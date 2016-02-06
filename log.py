def ln(x):
    size_ = len(str(int(x)))
    x /= x - 1
    sum = 0
    for i in range(1,100*10**size_):
        sum += 1/(i*x**i)
    return sum
