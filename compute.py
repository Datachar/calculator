
def calculate(data):
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
    if len(data) == 1:
        return data
    calc_md(data)
    if data[0] is '-':
        data[0] = float(data[1]) * (-1)
    result = float(data[0])
    data = data[1:]
    for elem in range(0, len(data)):
        if data[elem] == '+':
            result += float(data[elem+1])
        elif data[elem] == '-':
            result -= float(data[elem+1])
    return result

if __name__ == '__main__':
    #data = ['(', '1', '+', '3', ')', '/', '(', '4', '-', '3', ')']
    data = ['(', '7', '+', '3', ')', '*', '4']
    print(data)
    print(calculate(data))

