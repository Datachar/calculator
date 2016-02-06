def ln(x):
    if x == 0:
        return float('inf')
    if x > 1:
        size_ = len(str(int(x)))
        x /= x - 1
        if size_ > 6:
            size_ = 6
        sum = 0
        for i in range(1,20*10**size_):
            sum += 1/(i*x**i)
        return sum
    else:
        x = x-1
        sum = 0
        for i in range(1,10000):
            sum += ((-1)**(i+1)*x**i)/i
        return sum