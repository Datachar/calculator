def ln(x):
    sum_ = 0
    for i in range(0, 100000):
        sum_ += (1 / (2 * i + 1)) * ((x - 1) / (x + 1)) ** (2 * i + 1)
    return sum_ * 2
