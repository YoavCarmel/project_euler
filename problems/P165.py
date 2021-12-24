from typing import Tuple, Set

import numpy as np

FractionArray = Tuple[np.ndarray, np.ndarray]
FractionPointsArray = Tuple[FractionArray, FractionArray]
FractionPointFlat = Tuple[int, int, int, int]


# 2868868

def ans():
    lines_count = 5000
    quads = get_all_quads(get_all_tns(lines_count * 4))
    slopes = get_slopes(quads)
    consts = get_consts(quads, slopes)
    regular_inters = regular_intersect_all_lines(slopes, consts, quads)
    inf_slope_inters = inf_slope_intersect_all_lines(slopes, consts, quads)
    res = to_set(regular_inters, inf_slope_inters)
    return len(res)


def next_sn(curr) -> int:
    """
    :param curr: current sn
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


def get_all_quads(all_nums: np.ndarray) -> np.ndarray:
    # list of pairs of pairs of (x,y)
    return all_nums.reshape((-1, 2, 2))


def simplify_fraction_array(arr: FractionArray) -> FractionArray:
    n, d = arr
    gcd = np.gcd(n, d)
    both_neg = ((n < 0) & (d < 0))
    gcd[both_neg] = -gcd[both_neg]
    return n // gcd, d // gcd


def get_slopes(quads: np.ndarray) -> FractionArray:
    # m_n = y2 - y1, m_d = x2 - x1
    slopes = (quads[:, 0, :] - quads[:, 1, :])[:, ::-1]
    return simplify_fraction_array((slopes[:, 0], slopes[:, 1]))


def get_consts(quads: np.ndarray, slopes: FractionArray) -> FractionArray:
    # c_n = y1 * m_d - x1 * m_n, c_d = m_d
    slopes_n, slopes_d = slopes
    c_n = quads[:, 0, 1] * slopes_d - quads[:, 0, 0] * slopes_n
    c_d = slopes_d
    return simplify_fraction_array((c_n, c_d))


def regular_intersect_all_lines(slopes: FractionArray, consts: FractionArray, quads: np.ndarray) -> FractionPointsArray:
    x = calc_inters_x(slopes, consts)
    x = get_in_range(quads, x)
    y = calc_inters_y(slopes, consts, x)
    x, y = apply_abs(x, y)
    x, y = apply_tril(x, y)
    x_n_a, x_d_a = x
    y_n_a, y_d_a = y
    not_zero = (x_n_a != 0) & (x_d_a != 0) & (y_n_a != 0) & (y_d_a != 0)
    x_n_a = x_n_a[not_zero]
    x_d_a = x_d_a[not_zero]
    y_n_a = y_n_a[not_zero]
    y_d_a = y_d_a[not_zero]
    return (x_n_a, x_d_a), (y_n_a, y_d_a)


def calc_inters_x(slopes: FractionArray, consts: FractionArray) -> FractionArray:
    # unpack
    m_n, m_d = slopes
    c_n, c_d = consts
    # preps
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
    # unpack
    m_n, m_d = slopes
    c_n, c_d = consts
    x_n, x_d = x
    # calculate
    y_n = np.abs(x_n * (m_n * c_d) + x_d * (m_d * c_n))
    y_d = np.abs(x_d * (m_d * c_d))
    y_n, y_d = simplify_fraction_array((y_n, y_d))
    return y_n, y_d


def apply_abs(x: FractionArray, y: FractionArray) -> Tuple[FractionArray, FractionArray]:
    x = (np.abs(x[0]), np.abs(x[1]))
    y = (np.abs(y[0]), np.abs(y[1]))
    return x, y


def apply_tril(x: FractionArray, y: FractionArray) -> Tuple[FractionArray, FractionArray]:
    # unpack
    x_n, x_d = x
    y_n, y_d = y
    return (np.tril(x_n), np.tril(x_d)), (np.tril(y_n), np.tril(y_d))


def inf_slope_intersect_all_lines(slopes: FractionArray, consts: FractionArray, quads: np.ndarray) \
        -> FractionPointsArray:
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
    y_n = ((m_n * c_d) * inf_slope_x_values.reshape((-1, 1))) + (c_n * m_d)
    y_d = (m_d * c_d)
    y_n, y_d = simplify_fraction_array((y_n, y_d))
    # calc min_y, max_y of the inf slope lines
    inf_slope_y_values = inf_slope_quads[:, :, 1]
    inf_slope_min_y = np.min(inf_slope_y_values, axis=1)
    inf_slope_max_y = np.max(inf_slope_y_values, axis=1)
    # calc in_range bools:
    # inf slope min_max range
    all_lines_x_values = quads[:, :, 0]
    all_lines_in_x_range = (x_n > np.min(all_lines_x_values, axis=1)) & (x_n < np.max(all_lines_x_values, axis=1))
    min_y = y_n > (y_d * inf_slope_min_y.reshape((-1, 1)))
    max_y = y_n < (y_d * inf_slope_max_y.reshape((-1, 1)))
    together = min_y & max_y & all_lines_in_x_range
    # now convert to flat array of only wanted values
    x_n_a = x_n[together]
    x_d_a = x_d[together]
    y_n_a = y_n[together]
    y_d_a = y_d[together]
    return (x_n_a, x_d_a), (y_n_a, y_d_a)


def to_set(a1: FractionPointsArray, a2: FractionPointsArray) -> Set[FractionPointFlat]:
    x_n_a = np.concatenate((a1[0][0], a2[0][0]))
    x_d_a = np.concatenate((a1[0][1], a2[0][1]))
    y_n_a = np.concatenate((a1[1][0], a2[1][0]))
    y_d_a = np.concatenate((a1[1][1], a2[1][1]))
    return {quad_point for quad_point in zip(x_n_a, x_d_a, y_n_a, y_d_a)}
