from typing import Tuple, Set

import numpy as np

FractionArray = Tuple[np.ndarray, np.ndarray]  # (numerator, denominator)
FractionPointsArray = Tuple[FractionArray, FractionArray]  # (x FractionArray, y FractionArray)
FractionPointFlat = Tuple[int, int, int, int]  # (x_n, x_d, y_n, y_d)


def ans():
    lines_count = 5000
    quads = get_all_quads(lines_count)
    slopes = get_slopes(quads)
    consts = get_consts(quads, slopes)
    regular_inters = regular_intersect_all_lines(slopes, consts, quads)
    inf_slope_inters = inf_slope_intersect_all_lines(slopes, consts, quads)
    res = to_set(regular_inters, inf_slope_inters)
    return len(res)


def next_sn(curr) -> int:
    """
    :param curr: current s[n]
    :return: s[n+1]
    """
    return (curr * curr) % 50515093


def tn(sn) -> int:
    """
    :param sn: current sn
    :return: tn from sn
    """
    return sn % 500


def get_all_tns(limit) -> np.ndarray:
    """
    :param limit: max n value
    :return: a list of tn values
    """
    result: np.ndarray = np.zeros(limit, dtype="int64")
    sn = 290797
    for i in range(limit):
        sn = next_sn(sn)
        result[i] = tn(sn)
    return result


def get_all_quads(lines_count: int) -> np.ndarray:
    """
    :return: np array of size Nx2x2, of N lines, with each line being ((start_x, start_y), (end_x, end_y))
    """
    return get_all_tns(lines_count * 4).reshape((-1, 2, 2))


def simplify_fraction_array(arr: FractionArray) -> FractionArray:
    """
    :param arr: a FractionArray to simplify the numerator and denominator
    :return: the arr, simplified
    """
    n, d = arr
    gcd = np.gcd(n, d)
    both_neg = ((n < 0) & (d < 0))
    gcd[both_neg] = -gcd[both_neg]
    return n // gcd, d // gcd


def get_slopes(quads: np.ndarray) -> FractionArray:
    """
    :param quads: Nx2x2 np array of the lines
    :return: Nx2 FractionArray of slope of each of the N lines
    """
    """
    m = (y2-y1)/(x1-x2)
    ->
    m_n = y2 - y1
    m_d = x2 - x1
    """
    slopes = (quads[:, 0, :] - quads[:, 1, :])[:, ::-1]
    return simplify_fraction_array((slopes[:, 0], slopes[:, 1]))


def get_consts(quads: np.ndarray, slopes: FractionArray) -> FractionArray:
    """
    :param quads: Nx2x2 np array of the lines
    :param slopes: Nx2 FractionArray of the slopes
    :return: Nx2 FractionArray of constant of each of the N lines
    """
    # unpack
    slopes_n, slopes_d = slopes
    """
    y1 = mx1+c = (m_n/m_d)*x+c
    y1 = (m_n/m_d)*x1 + c
    c = y1 - (m_n/m_d)*x1
    c = y1 - (m_n*x1)/m_d
    c = (y1 * m_d - x1 * m_n)/m_d
    ->
    c_n = y1 * m_d - x1 * m_n
    c_d = m_d
    """
    c_n = quads[:, 0, 1] * slopes_d - quads[:, 0, 0] * slopes_n
    c_d = slopes_d
    return simplify_fraction_array((c_n, c_d))


def regular_intersect_all_lines(slopes: FractionArray, consts: FractionArray, quads: np.ndarray) -> FractionPointsArray:
    """
    :param slopes: Nx2 FractionArray of the slopes
    :param consts: Nx2 FractionArray of the constants
    :param quads: Nx2x2 FractionArray of the lines
    :return: FractionPointsArray of the intersections x and y values
    """
    x = calc_inters_x(slopes, consts)
    x = get_in_range(quads, x)
    y = calc_inters_y(slopes, consts, x)
    x, y = apply_abs(x, y)
    x, y = apply_tril(x, y)
    return get_actual_values(x, y, ((x[0] != 0) & (x[1] != 0) & (y[0] != 0) & (y[1] != 0)))


def calc_inters_x(slopes: FractionArray, consts: FractionArray) -> FractionArray:
    """
    :param slopes: Nx2 FractionArray of the slopes
    :param consts: Nx2 FractionArray of the constants
    :return: FractionArray of the x values of the intersections of the infinite lines of the slopes and consts
    """
    # unpack
    m_n, m_d = slopes
    c_n, c_d = consts
    # preps
    """
    m1*x+c1 = m2*x+c2
    x = (m1-m2)/(c2-c1)
    x = (m1_n/m1_d - m2_n/m2_d)/(c2_n/c2_d - c1_n/c1_d)
    x = ((c2_n*c1_d-c1_n*d2_d)/(c1_d*c2_d)) / ((m1_n*m2_d-m2_n*m1_d)/(m1_d*m2_d))
    x = (m1_d*m2_d*(c2_n*c1_d-c1_n*d2_d)) / (c1_d*c2_d*(m1_n*m2_d-m2_n*m1_d))
    ->
    x_n = m1_d*m2_d*(c2_n*c1_d-c1_n*d2_d)
    x_d = c1_d*c2_d*(m1_n*m2_d-m2_n*m1_d)
    
    BUT:
    m1=m2, c1=c2.
    the difference is that we should turn it to a matrix instead of a vector, to get all multiplications at once. 
    """
    m1_d_t_m2_d = m_d * (m_d.reshape((-1, 1)))
    c1_d_t_c2_d = c_d * (c_d.reshape((-1, 1)))
    m1_d_t_m2_n = m_d * (m_n.reshape((-1, 1)))
    m1_n_t_m2_d = m_n * (m_d.reshape((-1, 1)))
    c1_d_t_c2_n = c_d * (c_n.reshape((-1, 1)))
    c1_n_t_c2_d = c_n * (c_d.reshape((-1, 1)))
    # calculate
    x_n = m1_d_t_m2_d * (c1_d_t_c2_n - c1_n_t_c2_d)
    x_d = c1_d_t_c2_d * (m1_n_t_m2_d - m1_d_t_m2_n)
    x_n, x_d = simplify_fraction_array((x_n, x_d))
    return x_n, x_d


def get_in_range(quads: np.ndarray, x: FractionArray) -> FractionArray:
    """
    make 0 all the x intersection values that are out of the range of their lines
    :param quads: Nx2x2 FractionArray of the lines
    :param x: FractionArray of the intersection x values
    :return: the FractionArray after zeroing all x values out of their lines pair ranges
    """
    # unpack
    x_n, x_d = x
    # preps
    quads_x = quads[:, :, 0]
    min_x_quads = np.min(quads_x, axis=1)
    max_x_quads = np.max(quads_x, axis=1)
    # bools
    min_x = (x_n > x_d * min_x_quads)
    max_x = (x_n < x_d * max_x_quads)
    x_in_range = min_x & max_x
    x_in_range_sym = x_in_range & x_in_range.T
    # apply
    x_n[~x_in_range_sym] = 0
    x_d[~x_in_range_sym] = 0
    return x


def calc_inters_y(slopes: FractionArray, consts: FractionArray, x: FractionArray) -> FractionArray:
    """
    calculate the y values of the x values of the intersections
    :param slopes: Nx2 FractionArray of the slopes
    :param consts: Nx2 FractionArray of the constants
    :param x: FractionArray of the intersection x values
    :return: FractionArray of the intersection y values
    """
    # unpack
    m_n, m_d = slopes
    c_n, c_d = consts
    x_n, x_d = x
    # calculate
    """
    y = mx+c
    y = (m_n/m_d)*(x_m/x_d)+(c_n/c_d)
    y = (m_n*x_n)/(m_d*x_d)+(c_n*c_d)
    y = (m_n*x_n*c_d + m_d*x_d*c_n) / (m_d*x_d*c_d)
    ->
    y_n = m_n*x_n*c_d + m_d*x_d*c_n
    y_d = m_d*x_d*c_d
    
    BUT:
    x,y are matrices of all pairs.
    m,c are vectors, one entry per line.
    the nice part is that using m1,c1 or m2,c2 should not change the result of the y calculation.
    so, we can just use any one of the lines' m,c for the y calculation.
    so, when multiplying the x matrix by m,c, as long as each of the cells in the x matrix gets tm,c of the same line,
    and this line is any one of the lines it is on, the result should be correct.
    """
    y_n = x_n * (m_n * c_d) + x_d * (m_d * c_n)
    y_d = x_d * (m_d * c_d)
    y_n, y_d = simplify_fraction_array((y_n, y_d))
    return y_n, y_d


def apply_abs(x: FractionArray, y: FractionArray) -> Tuple[FractionArray, FractionArray]:
    """
    apply absolute value on the x,y values, as we know 0<x,y<500 and dont want something like (-5/-3)->(5/3)
    :param x: FractionArray of the intersection x values
    :param y: FractionArray of the intersection y values
    :return: the same parameters but after applying np.abs
    """
    # unpack
    x_n, x_d = x
    y_n, y_d = y
    return (np.abs(x_n), np.abs(x_d)), (np.abs(y_n), np.abs(y_d))


def apply_tril(x: FractionArray, y: FractionArray) -> Tuple[FractionArray, FractionArray]:
    """
    there are currently duplications of values -
    each intersection point appears both in the upper and lower triangle.
    eliminate one of each of the duplicates
    :param x: FractionArray of the intersection x values
    :param y: FractionArray of the intersection y values
    :return: the same parameters after eliminating the duplicates
    """
    # unpack
    x_n, x_d = x
    y_n, y_d = y
    return (np.tril(x_n), np.tril(x_d)), (np.tril(y_n), np.tril(y_d))


def get_actual_values(x: FractionArray, y: FractionArray, bools: np.ndarray) -> FractionPointsArray:
    """
    get the actual values that pass the bools test, in a flat array
    :param x: FractionArray of the intersection x values
    :param y: FractionArray of the intersection y values
    :param bools: np.ndarray of bools to apply on the array parameters
    :return: FractionPointsArray of the actual points, without all the 0s
    """
    x_n_a, x_d_a = x
    y_n_a, y_d_a = y
    return (x_n_a[bools], x_d_a[bools]), (y_n_a[bools], y_d_a[bools])


def inf_slope_intersect_all_lines(slopes: FractionArray, consts: FractionArray, quads: np.ndarray) \
        -> FractionPointsArray:
    """
    the regular intersection returns 0 for all lines that have an infinite slope,
    so this function calculate their intersections with all lines in the right way
    :param slopes: Nx2 FractionArray of the slopes
    :param consts: Nx2 FractionArray of the constants
    :param quads: Nx2x2 FractionArray of the lines
    :return: FractionPointsArray of the intersections x and y values with the infinite slope lines
    """
    # unpack
    m_n, m_d = slopes
    c_n, c_d = consts
    # calc x values of inf slope lines
    inf_slope_indices = slopes[1] == 0
    inf_slope_quads = quads[inf_slope_indices]
    inf_slope_x_values = inf_slope_quads[:, 0, 0]  # x of the first point, equals the x of other point so doesnt matter
    # now simulate x
    x_n = np.ones((len(inf_slope_x_values), len(quads)), dtype="int64") * inf_slope_x_values.reshape((-1, 1))
    x_d = np.ones((len(inf_slope_x_values), len(quads)), dtype="int64")
    # calc the y values of all lines in these x values
    """
    exact same calculation as in the calc_inters_y() function,
    except that now it easier because x is not split to x_n,x_d.
    
    ALSO:
    x is not a matrix now. it is only a vector.
    we want a matrix with each of the x values treated for its whole own row.
    so reshaping x is a correct way to do that.
    """
    y_n = ((m_n * c_d) * inf_slope_x_values.reshape((-1, 1))) + (c_n * m_d)
    y_d = (m_d * c_d)
    y_n, y_d = simplify_fraction_array((y_n, y_d))
    # calc min_y, max_y of the inf slope lines
    inf_slope_y_values = inf_slope_quads[:, :, 1]
    inf_slope_min_y = np.min(inf_slope_y_values, axis=1)
    inf_slope_max_y = np.max(inf_slope_y_values, axis=1)
    # calc in_range bools:
    """
    we want:
    result y value is inside the ranges of the inf slope line
    x values is inside the ranges of the regular line 
    """
    all_lines_x_values = quads[:, :, 0]
    all_lines_in_x_range = (x_n > np.min(all_lines_x_values, axis=1)) & (x_n < np.max(all_lines_x_values, axis=1))
    min_y = y_n > (y_d * inf_slope_min_y.reshape((-1, 1)))
    max_y = y_n < (y_d * inf_slope_max_y.reshape((-1, 1)))
    together = min_y & max_y & all_lines_in_x_range
    return get_actual_values((x_n, x_d), (y_n, y_d), together)


def to_set(regular_inters: FractionPointsArray, inf_slope_inters: FractionPointsArray) -> Set[FractionPointFlat]:
    """
    convert the result points to a set, to eliminate duplications, as the question require.
    :param regular_inters: FractionPointsArray of the regular intersections
    :param inf_slope_inters: FractionPointsArray of the infinite slope intersections
    :return: a set of quads of all the intersection points together
    """
    # tuple access is base on the known conventions of order of arrays
    x_n_a = np.concatenate((regular_inters[0][0], inf_slope_inters[0][0]))
    x_d_a = np.concatenate((regular_inters[0][1], inf_slope_inters[0][1]))
    y_n_a = np.concatenate((regular_inters[1][0], inf_slope_inters[1][0]))
    y_d_a = np.concatenate((regular_inters[1][1], inf_slope_inters[1][1]))
    return {quad_point for quad_point in zip(x_n_a, x_d_a, y_n_a, y_d_a)}
