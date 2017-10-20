from stack import Stack


def infix_to_postfix(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opstack = Stack()
    postfix_list = []
    tokens = infix_expr.split()

    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = opstack.pop()
        else:
            while (not opstack.is_empty()) and prec[opstack.peek()] >= prec[token]:
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.is_empty():
        postfix_list.append(opstack.pop())

    return ' '.join(postfix_list)


def postfix_eval(expr):
    opstack = Stack()
    expr = infix_to_postfix(expr)
    tokens = expr.split()

    for token in tokens:
        if token in '0123456789':
            opstack.push(int(token))
        else:
            op2 = opstack.pop()
            op1 = opstack.pop()
            result = do_math(token, op1, op2)
            opstack.push(result)
    return opstack.pop()


def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':

    print(postfix_eval('5 + 6 * 7'))
