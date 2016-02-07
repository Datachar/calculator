from compute import calculate

def calc_eq(data):
    k = data.index('=')
    left_part = data[:k]
    right_part = data[k+1:]

    if 'x' in left_part:
        data_with_x = left_part
        data = right_part
    else:
        data_with_x = right_part
        data = left_part
    x_index = data_with_x.index('x')

    if len(right_part) > 1:
        right_part = calculate(right_part)
    right_part = float(right_part[0])

    if x_index > 0 and data_with_x[x_index-1] == '*' or data_with_x[x_index-1] == '/':
        act_data = data_with_x[x_index-1]
        act_data_index = x_index - 1
    else:
        act_data = data_with_x[x_index+1]
        act_data_index = x_index + 1

    if data_with_x[act_data_index-1] == ')':
        for i in range((act_data_index-1), -1, -1):

            if data_with_x[i] == '(':
                data_near_x = []
                data_near_x.append(calculate(data_with_x[i:act_data_index]))

                data_with_x[i:act_data_index] = data_near_x
                data_near_x = data_near_x[0]
    else:
        if act_data_index < x_index:
            data_near_x = data_with_x[act_data_index-1]
        else:
            data_near_x = data_with_x[act_data_index+1]

    data_without_x = 0

    if len(data_with_x) > 3:
        data_with_x.remove(data_near_x)
        data_with_x.remove(act_data)
        data_with_x.remove('x')
        data_without_x = calculate(data_with_x)
    if data_without_x > 0:
        right_part -= data_without_x
    else:
        right_part += data_without_x


    if act_data == '*':
        result = right_part / float(data_near_x)
    elif act_data == '/':
        result = right_part * float(data_near_x)
    return result
'''
if __name__ == '__main__':
    data = ['(', '7', '+', '1', ')', '*', 'x', '=', '6']
    data = ['x', '*', '2', '+', '0.5', '=', '1' ]    #2 * x + 0.5 = 1
    calk(data)
    '''

