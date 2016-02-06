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
        data = str_to_list(input_data)
        result = calculate(data)
        print('output: %d' % result)
except ZeroDivisionError:
    print('bad input(divide on 0)')
except ValueError:
    print('bad input')
