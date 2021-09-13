from libs.calculations import inverse_mod


def ans():
    a = 1504170715041707
    b = 4503599627370517
    # for n=3451657199285664 we get (a*n)%b=1 and we can stop
    """
    i cant prove it, but analyzing the first results:
    []		1		1504170715041707
    [3]		3		8912517754604
    [2, 168]		506		2044785486369
    [2, 167, 4]		2527		1311409677241
    [2, 167, 3, 1]		4548		578033868113
    [2, 167, 3, 0, 2]		11117		422691927098
    [2, 167, 3, 0, 1, 1]		17686		267349986083
    [2, 167, 3, 0, 1, 0, 1]		24255		112008045068
    [2, 167, 3, 0, 1, 0, 0, 2]		55079		68674149121
    [2, 167, 3, 0, 1, 0, 0, 1, 1]		85903		25340253174
    [2, 167, 3, 0, 1, 0, 0, 1, 0, 2]		202630		7346610401
    [2, 167, 3, 0, 1, 0, 0, 1, 0, 1, 3]		724617		4046188430
    [2, 167, 3, 0, 1, 0, 0, 1, 0, 1, 2, 1]		1246604		745766459
    [2, 167, 3, 0, 1, 0, 0, 1, 0, 1, 2, 0, 5]		6755007		428410324
    
    where product of ni*vi for:
        ni=n of ci'th coin
        vi=i'th value of the list
    results in n_(i+1).
    furthermore, decreasing 1 from the last ni, and running the loop on the multiples of the new ni,
    looks like results in the next ni.
    try to implement it
    """
    min_coin = b
    s = 0
    n = 1
    max_n = 1
    while min_coin > 1:
        coin = (a * n) % b
        if coin < min_coin:
            min_coin = coin
            s += coin
            n, max_n = n - max_n, n
        n += max_n
    return s


def analyze():
    a = 1504170715041707
    b = 4503599627370517
    min_coin = b
    s = 0
    n = 1
    by_now = list()
    while min_coin > 1:
        coin = (a * n) % b
        if coin < min_coin:
            min_coin = coin
            s += coin
            print(list(reversed(get_seq(n, reversed(by_now)))), n, coin, sep="\t")
            by_now.append(n)
        n += 1
    return s


def get_seq(target, nums):
    ll = list()
    for num in nums:
        ll.append(target // num)
        target %= num
    return ll
