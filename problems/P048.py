def ans():
    s=0
    limit=1000
    for i in range(1,limit+1):
        s+=(i**i)
    return s%(10**10)