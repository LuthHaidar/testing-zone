def mult(a, b):
    if b == 0:
        return 0
    return a + mult(a, b - 1)

mult(3, 6)