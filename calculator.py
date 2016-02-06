from str_to_list import str_to_list
from compute import calculate
from log import ln

try:
    input_data = str(input('input: '))
    if 'log' in input_data:
        i = input_data.index('(')
        k = input_data.index(')')
        data = float(input_data[i+1:k])
        #print(data)
        result = ln(data)
        print('output: %s' % result)
    else:
        if input_data == '':
            raise ValueError
        n = len(input_data) - 1
        for i in range(0, n):
            if input_data[i].isdigit() and input_data[i+2].isdigit() and input_data[i+1] == ' ':
                raise ValueError
            if input_data[i].isalpha():
                raise ValueError
        data = str_to_list(input_data)
        result = calculate(data)
        print('output: %d' % result)
except ZeroDivisionError:
    print('bad input(divide on 0)')
except ValueError:
    print('bad input')
