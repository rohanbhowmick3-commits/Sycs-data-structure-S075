def prefixToPostfix(exp):

    stack = []

    operators = "+-*/^"

    for ch in reversed(exp):

        if ch not in operators:
            stack.append(ch)

        else:
            a = stack.pop()
            b = stack.pop()

            stack.append(a + b + ch)

    return stack[0]

expression = input("Enter Prefix Expression: ")

print("Postfix:", prefixToPostfix(expression))