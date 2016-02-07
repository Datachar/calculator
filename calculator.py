from str_to_list import str_to_list
from compute import calculate
from log import log

def calculator(data):
    try:
        #input_data = str(input('input: '))
        input_data = data
        if 'log' in input_data:
            i = input_data.index('(')
            k = input_data.index(')')
            data = float(input_data[i+1:k])
            result = log(data)
            return result
            #print('output: %s' % result)
        else:
            data = str_to_list(input_data)
            result = calculate(data)
            #print('output: %d' % result)
            return result

    except ZeroDivisionError:
        print('bad input')

    except ValueError:  
        print('bad input')
