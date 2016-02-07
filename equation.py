from calculator import calculator

def calk(data):
    k = data.index('=')
    left_part = data[:k]
    right_part = data[k+1:]
    #print(left_part)
    #print(right_part)
    if 'x' in left_part:
        data_with_x = left_part
        data = right_part
    else:
        data_with_x = right_part
        data = left_part
    x_index = data_with_x.index('x')

    if len(right_part) > 1:
        right_part = calculator(right_part)
    right_part = float(right_part[0])

    if x_index > 0 and data_with_x[x_index-1] == '*' or data_with_x[x_index-1] == '/':
        act_data = data_with_x[x_index-1]
        act_data_index = x_index - 1
    else:
        act_data = data_with_x[x_index+1]
        act_data_index = x_index + 1

    if data_with_x[act_data_index-1] == ')':
        for i in range((act_data_index-1), -1, -1):
            #print(data_with_x)
            #print(i)
            if data_with_x[i] == '(':
                data_near_x = []
                data_near_x.append(calculator(data_with_x[i:act_data_index]))
                #print('d:', data_near_x)
                data_with_x[i:act_data_index] = data_near_x
                data_near_x = data_near_x[0]
    else:
        if act_data_index < x_index:
            data_near_x = data_with_x[act_data_index-1]
        else:
            data_near_x = data_with_x[act_data_index+1]

    data_without_x = 0
    #print('da', data_near_x)
    if len(data_with_x) > 3:
        data_with_x.remove(data_near_x)
        data_with_x.remove(act_data)
        data_with_x.remove('x')
        data_without_x = calculator(data_with_x)
    if data_without_x > 0:
        right_part -= data_without_x
    else:
        right_part += data_without_x
    #print('data w: ', data_without_x)

    #print('data:', data_with_x)
    #print(data_near_x)

    if act_data == '*':
        result = right_part / float(data_near_x)
    elif act_data == '/':
        result = right_part * float(data_near_x)
    print('result:', result)

if __name__ == '__main__':
    data = ['(', '7', '+', '1', ')', '*', 'x', '=', '6']
    data = ['x', '*', '2', '+', '0.5', '=', '1' ]    #2 * x + 0.5 = 1
    calk(data)

