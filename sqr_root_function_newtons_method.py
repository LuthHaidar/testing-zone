def sqrt(n):
    x = n # initial guess
    while (True):
        rt = 0.5 * (x + (n / x)) # new guess
        if (((rt - x) ** 2) ** 0.5) < 0.0000000001: # check if the difference between the new guess and the old guess is less than 0.0000000001
            break
        x = rt # update the old guess
    return rt