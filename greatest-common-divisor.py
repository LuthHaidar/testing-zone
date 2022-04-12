def greatestcommondivisor(a, b):
    if b == 0:
        return a
    else:
        return greatestcommondivisor(b, a % b)