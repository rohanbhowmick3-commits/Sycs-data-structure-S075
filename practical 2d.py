stack = []

while True:

    print("\n1.Type")
    print("2.Undo")
    print("3.Show")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        text = input("Enter Text: ")
        stack.append(text)

    elif ch == 2:
        if len(stack) == 0:
            print("Nothing to Undo")
        else:
            print("Removed:", stack.pop())

    elif ch == 3:
        print("Current Data:", stack)

    elif ch == 4:
        break