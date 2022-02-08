def sqrt(n):
    x = n
    while (True):
        rt = 0.5 * (x + (n / x))
        if (((rt - x) ** 2) ** 0.5) < 0.0000000001:
            break
        x = rt
    return rt