from libs.numbers_properties import num_size
from libs.polygon_numbers import is_polygonal_number, is_any_polygon_number, all_polygons_fit_to_number


def ans():
    polygons = [3, 4, 5, 6, 7, 8]
    NOT_FOUND = 0

    def next_in_chain(chain, left):
        if len(chain) == 5:
            last_in_chain = (chain[len(chain) - 1] % 100) * 100 + chain[0] // 100
            if is_polygonal_number(last_in_chain, left[0]) and num_size(last_in_chain) == 4:
                chain.append((chain[len(chain) - 1] % 100) * 100 + chain[0] // 100)
                return chain
        elif len(chain) == 0:
            for i in range(1000, 10000):
                if is_any_polygon_number(i, left):
                    chain.append(i)
                    for s in all_polygons_fit_to_number(i, polygons):
                        if s in left:
                            left.remove(s)
                            result_chain = next_in_chain(chain.copy(), left.copy())
                            if result_chain != NOT_FOUND:
                                return result_chain
                            left.append(s)
                    chain.remove(i)
        else:
            last = chain[-1]
            if last % 100 >= 10:
                for i in range((last % 100) * 100, (last % 100 + 1) * 100):
                    if is_any_polygon_number(i, left):
                        chain.append(i)
                        for s in all_polygons_fit_to_number(i, polygons):
                            if s in left:
                                left.remove(s)
                                result_chain = next_in_chain(chain.copy(), left.copy())
                                if result_chain != NOT_FOUND:
                                    return result_chain
                                left.append(s)
                        chain.remove(i)
        return NOT_FOUND

    return sum(next_in_chain([], polygons.copy()))
