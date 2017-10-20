from stack import Stack


def is_balanced(expr):
    """  Time Complexity: O(n)
    Auxiliary Space: O(n) for stack

    """

    opening = set('([{')
    match = set([('(', ')'), ('[', ']'), ('{', '}')])
    s = Stack()

    for char in expr:
        if char in opening:
            s.push(char)
        else:
            if s.size() == 0:
                return 'Not Balanced'
            else:
                topchar = s.pop()
                if (topchar, char) not in match:
                    return 'Not Balanced'

    return 'Balanced' if s.size() == 0 else 'Not Balanced'


test_strings = ['{[()]}', '{[(])}', '{{[[(())]]}}']

for test in test_strings:
    print(is_balanced(test))
