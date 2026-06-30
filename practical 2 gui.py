import tkinter as tk
from tkinter import messagebox

# =========================
# STACK USING ARRAY
# =========================
stack = []

def stack_array_gui():
    win = tk.Toplevel(root)
    win.title("Practical 1 - Stack Using Array")
    win.geometry("400x450")

    tk.Label(win, text="Enter Element", font=("Arial", 12)).pack(pady=5)

    entry = tk.Entry(win, width=20, font=("Arial", 12))
    entry.pack()

    output = tk.Text(win, height=12, width=40)
    output.pack(pady=10)

    def refresh():
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Current Stack\n")
        output.insert(tk.END, "-----------------\n")

        if len(stack) == 0:
            output.insert(tk.END, "Stack Empty")
        else:
            for item in reversed(stack):
                output.insert(tk.END, str(item) + "\n")

    def push():
        value = entry.get()

        if value == "":
            messagebox.showwarning("Warning", "Enter an element")
            return

        stack.append(value)
        entry.delete(0, tk.END)
        refresh()

    def pop():
        if len(stack) == 0:
            messagebox.showerror("Error", "Stack Underflow")
        else:
            value = stack.pop()
            messagebox.showinfo("Deleted", f"{value} removed")
            refresh()

    def peek():
        if len(stack) == 0:
            messagebox.showinfo("Peek", "Stack Empty")
        else:
            messagebox.showinfo("Top Element", stack[-1])

    tk.Button(win, text="Push", width=15, command=push).pack(pady=5)
    tk.Button(win, text="Pop", width=15, command=pop).pack(pady=5)
    tk.Button(win, text="Peek", width=15, command=peek).pack(pady=5)
    tk.Button(win, text="Display", width=15, command=refresh).pack(pady=5)

    refresh()

# =========================
# PLACEHOLDER FUNCTIONS
# =========================

def linked_list_gui():
    messagebox.showinfo("Coming Soon", "Practical 2")

def delimiter_gui():
    messagebox.showinfo("Coming Soon", "Practical 3")

def undo_gui():
    messagebox.showinfo("Coming Soon", "Practical 4")

def prefix_gui():
    messagebox.showinfo("Coming Soon", "Practical 5")

def postfix_gui():
    messagebox.showinfo("Coming Soon", "Practical 6")

# =========================
# MAIN MENU
# =========================

root = tk.Tk()
root.title("Stack Practical GUI")
root.geometry("350x420")

tk.Label(
    root,
    text="DATA STRUCTURE PRACTICALS",
    font=("Arial", 15, "bold")
).pack(pady=15)

tk.Button(root, text="1. Stack Using Array",
          width=30, command=stack_array_gui).pack(pady=5)

tk.Button(root, text="2. Stack Using Linked List",
          width=30, command=linked_list_gui).pack(pady=5)

tk.Button(root, text="3. Delimiter Matching",
          width=30, command=delimiter_gui).pack(pady=5)

tk.Button(root, text="4. Undo Mechanism",
          width=30, command=undo_gui).pack(pady=5)

tk.Button(root, text="5. Prefix → Postfix",
          width=30, command=prefix_gui).pack(pady=5)

tk.Button(root, text="6. Postfix Evaluation",
          width=30, command=postfix_gui).pack(pady=5)

tk.Button(root, text="Exit",
          width=30, command=root.destroy).pack(pady=20)

root.mainloop()