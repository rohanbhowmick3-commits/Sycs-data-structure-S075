def check(expression):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:

        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if len(stack) == 0:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

exp = input("Enter Expression: ")

if check(exp):
    print("Balanced")
else:
    print("Not Balanced")