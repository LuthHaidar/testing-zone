def hailstone(n):
    
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    
    x = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            n = (n * 3) + 1
        x = x + 1
        print (n)
    
    return x + 1