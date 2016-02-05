

def main(data):
    while '(' in data:
        tmp =  calc_with_brackets(data)


def calc_with_brackets(data):
    res = []
    n = len(data) - 1
    for i in range(n-1, 0, -1):
        if data[i] == '(':
            k = data.index(')')
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
    calc_md(data)
    result = int(data[0])
    data = data[1:]
    for elem in range(0, len(data)):
        if data[elem] == '+':
            result += int(data[elem+1])
        elif data[elem] == '-':
            result -= int(data[elem+1])
    return result

if __name__ == '__main__':
    print(compute(['1', '+', '2', '/', '2']))
    print(calc_with_brackets(['1' ' + ','(','4','-','2',')',]))
