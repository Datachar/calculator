def str_to_list(expression):
    expression_l = list(expression)
    return negative_mul_for_first(gluing_log(gluing_float_numbers(gluing_numbers(remove_space(expression_l)))))


def remove_space(expression_l):
    i = 0
    while i != len(expression_l):
        if expression_l[i] == ' ':
            expression_l.pop(i)
        else:
            i += 1
    if len(expression_l) == 0:
        return expression_l
    return expression_l


def gluing_numbers(expression_l):
    i = 0
    number_l = list(range(10))
    op = False
    while i != len(expression_l):
        if expression_l[i] in str(number_l) or op == True:
            if i + 1 == len(expression_l):
                break
            elif expression_l[i + 1] in str(number_l):
                expression_l[i] = expression_l[i] + expression_l[i + 1]
                expression_l.pop(i + 1)
                op = True
            else:
                i += 1
                op = False
        else:
            i += 1
            op = False
    return expression_l


def gluing_float_numbers(expression_l):
    i = 0
    while i != len(expression_l):
        if expression_l[i] == '.':
            s = expression_l[i]
            expression_l.pop(i)
            i -= 1
            while expression_l[i + 1] == '.':
                s = s + expression_l[i + 1]
                expression_l.pop(i + 1)
            if (i != len(expression_l)) or i != 0:
                expression_l[i] = expression_l[i] + s + expression_l[i + 1]
                expression_l.pop(i + 1)
        i += 1
    return expression_l


def gluing_log(expression_l):
    i = 0
    while i != len(expression_l):
        if expression_l[i] == 'l':
            if expression_l[i + 1] != len(expression_l) and \
                            expression_l[i + 1] == 'o':
                if expression_l[i + 2] != len(expression_l) and \
                                expression_l[i + 2] == 'g':
                    if expression_l[i + 3] != len(expression_l) and \
                                    expression_l[i + 3] == '(':
                        expression_l[i] = expression_l[i] + expression_l[i + 1] \
                                          + expression_l[i + 2] + expression_l[i + 3]
                        expression_l.pop(i + 1)
                        expression_l.pop(i + 1)
                        expression_l.pop(i + 1)
        i += 1
    return expression_l


def negative_mul_for_first(expression_l):
    if expression_l[0] == '-':
        if len(expression_l) > 3 and (expression_l[2] == '*' or expression_l[2] == '/'):
            expression_l.insert(0, '(')
            expression_l.insert(3, ')')
    return expression_l
