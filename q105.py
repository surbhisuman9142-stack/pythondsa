def evaluate(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = int( left / right)
            stack.append(result)
    return stack[-1]
tokens = ["2", "1", "+", "3", "*"]
print(evaluate(tokens))  