
def calculate(data):
    left_b = 0
    right_b = 0
    for i in data:
        if i == '(':
            left_b += 1
        elif i == ')':
            right_b += 1
    if left_b != right_b:
        raise ValueError
    for i in data:
        if data[0] == '(' and data[-1] == ')':
            data = data[1:-1]
    tmp = data
    while '(' in tmp:
        tmp = calc_with_brackets(data)
    result = compute(tmp)
    return result

def calc_with_brackets(data):
    res = []
    i = len(data)
    k = i - 1
    while i > 0:
        i -= 1
        if data[i] == '(':
            k = data.index(')')
            if i < k:
                res = data[i+1:k]
                res_compute = str(compute(res))
                tmp = []
                tmp.append(res_compute)
                data[i:k+1] = tmp
    return data

def calc_md(data):
    while '*' in data or '/' in data:
        if '*' in data:
            k = data.index('*')
            res = float(data[k-1]) * float(data[k+1])
            tmp = []
            tmp.append(res)
            data[k-1:k+2] = tmp
        elif '/' in data:
            k = data.index('/')
            res = float(data[k-1]) / float(data[k+1])
            tmp = []
            tmp.append(res)
            data[k-1:k+2] = tmp
        else:
            return data
    return data

def compute(data):
    for i in data:
        if i.isalpha():
            raise ValueError
        '''
    if data[0] == '(' and data[-1] == ')':
        data = data[1:-1]
        '''
    if len(data) == 1:
        return float(data[0])
    calc_md(data)
    if data[0] is '-':
        data[0] = float(data[1]) * (-1)
    elif data[0] is '+':
        data[0] = float(data[1])
    result = float(data[0])
    data = data[1:]
    for elem in range(0, len(data)):
        if data[elem] == '+':
            result += float(data[elem+1])
        elif data[elem] == '-':
            result -= float(data[elem+1])
    return result
