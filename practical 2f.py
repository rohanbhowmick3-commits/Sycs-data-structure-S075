def evaluate(exp):
    stack = []

    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))

        elif ch in "+-*/":
            if len(stack) < 2:
                return "Invalid Postfix Expression"

            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
        elif ch == " ":
            continue
        else:
            return "Invalid Character"

    if len(stack) != 1:
        return "Invalid Postfix Expression"

    return stack.pop()

expression = input("Enter Postfix Expression: ")
print("Answer:", evaluate(expression))