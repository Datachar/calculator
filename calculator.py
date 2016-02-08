from str_to_list import str_to_list
from compute import calculate
from log import log
from equation import calc_eq

def calculator(data):
    try:
        if '=' in data:
            data = str_to_list(data)
            result = calc_eq(data)
            if result == 'error':
                raise ValueError
            else:
                result = 'x = ' + str(result)
                return result

        input_data = data
        if 'log' in input_data:
            i = input_data.index('(')
            k = input_data.index(')')
            data = float(input_data[i+1:k])
            result = log(data)
            return result
        else:
            data = str_to_list(input_data)
            result = calculate(data)
            return result

    except ZeroDivisionError:
        print('bad input')
        exit()
    except ValueError:  
        print('bad input')
        exit()

input_data = str(input('input: '))
print(calculator(input_data))
