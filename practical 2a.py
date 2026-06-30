class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "inserted")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Deleted:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element:", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", self.stack)

s = Stack()

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter element: ")
        s.push(x)

    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.peek()

    elif ch == 4:
        s.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")