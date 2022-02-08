def luhn(n):
    sumh = 0
    m = n # made a copy of n
    while m > 0:  # part 1: sum all the digits   n .. n-1 .. n-1 .... 2  ..1
        sumh += m % 10
        m = m // 10
    while n > 0: #part 2: abcdef
        x = n % 100 #ef
        x = x // 10 #e
        n = n // 100 #abcd
        if x < 5: #part 3: 
            sumh += x
        else:
            sumh += x - 9
    if sumh % 10 == 0:
        return True
    else:
        return False
