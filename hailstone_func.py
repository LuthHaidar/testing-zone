def hailstone(n):
    x = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            n = (n * 3) + 1
        x = x + 1
        print (n)
    return x + 1
