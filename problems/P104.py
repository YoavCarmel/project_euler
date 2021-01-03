from libs.numbers_properties import is_pandigital


def ans():
    print("takes about 16 seconds")
    fn = 1
    fnm = 1
    k = 3
    last_ten_digs = 10 ** 9
    while True:
        fnp = fn + fnm
        fnm = fn
        fn = fnp
        if is_pandigital(fn % last_ten_digs, 9) and is_pandigital(int(str(fn)[:9]), 9):
            return k
        k += 1
