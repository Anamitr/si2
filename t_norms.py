def lukasiewicz_t(x, y):
    return max(x + y - 1.0, 0)


def fodor_t(x, y):
    if x + y > 1:
        return min(x, y)
    else:
        return 0


def drastic_t(x, y):
    if x == 1:
        return y
    elif y == 1:
        return x
    else:
        return 0


def einstein_t(x, y):
    return (x * y) / (2 - (x + y - x * y))
