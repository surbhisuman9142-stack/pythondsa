def calc(expr):
    a , op ,b = expr.split()
    a , b = float(a) , float(b)
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    raise ValueError('unknown op')
print(calc("6 / 4"))
