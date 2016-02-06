def str_to_list(expression):
    expression = list(expression)
    expression = remove_space(expression)
    expression = gluing_numbers(expression)
    expression = gluing_float_numbers(expression)
    expression = gluing_log(expression)
    expression = negative_mul_for_first(expression)
    return expression


def remove_space(expression):
    return [char for char in expression if char != ' ']


def gluing_numbers(expression):
    i = 0
    number = list(range(10))
    op = False
    while i != len(expression):
        if expression[i] in str(number) or op == True:
            if i + 1 == len(expression):
                break
            elif expression[i + 1] in str(number):
                expression[i] = expression[i] + expression[i + 1]
                expression.pop(i + 1)
                op = True
            else:
                i += 1
                op = False
        else:
            i += 1
            op = False
    return expression


def gluing_float_numbers(expression):
    i = 0
    while i != len(expression):
        if expression[i] == '.':
            s = expression[i]
            expression.pop(i)
            i -= 1
            while expression[i + 1] == '.':
                s = s + expression[i + 1]
                expression.pop(i + 1)
            if (i != len(expression)) or i != 0:
                expression[i] = expression[i] + s + expression[i + 1]
                expression.pop(i + 1)
        i += 1
    return expression


def gluing_log(expression):
    i = 0
    while i != len(expression):
        if expression[i] == 'l':
            if expression[i + 1] != len(expression) and \
                            expression[i + 1] == 'o':
                if expression[i + 2] != len(expression) and \
                                expression[i + 2] == 'g':
                    if expression[i + 3] != len(expression) and \
                                    expression[i + 3] == '(':
                        expression[i] = expression[i] + expression[i + 1] \
                                        + expression[i + 2] + expression[i + 3]
                        expression.pop(i + 1)
                        expression.pop(i + 1)
                        expression.pop(i + 1)
        i += 1
    return expression


def negative_mul_for_first(expression):
    if expression[0] == '-':
        if len(expression) > 3 and (expression[2] == '*' or expression[2] == '/'):
            expression.insert(0, '(')
            expression.insert(3, ')')
    return expression