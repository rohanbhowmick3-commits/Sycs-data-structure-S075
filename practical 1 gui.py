import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return " <- ".join(reversed(self.items)) if self.items else "Stack is empty"


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Interactive Stack GUI")
        self.root.state("zoomed")
        self.root.configure(bg="#1f2533")
        self.build_ui()

    def build_ui(self):
        header = tk.Frame(self.root, bg="#1f2533")
        header.pack(fill="x", pady=(15, 0))

        tk.Label(
            header,
            text="Interactive Stack Operations",
            font=("Segoe UI", 16, "bold"),
            bg="#1f2533",
            fg="#f5f7ff"
        ).pack()

        tk.Label(
            self.root,
            text="Enter an item to push into the stack",
            font=("Segoe UI", 10),
            bg="#1f2533",
            fg="#d3d8e6"
        ).pack(pady=(10, 5))

        self.entry = tk.Entry(self.root, width=28, font=("Segoe UI", 12), bd=0, relief="solid")
        self.entry.pack(pady=(0, 10), ipadx=6, ipady=6)

        self.status_label = tk.Label(
            self.root,
            text="Stack is empty.",
            font=("Segoe UI", 10),
            bg="#1f2533",
            fg="#8ab4f8"
        )
        self.status_label.pack(pady=(0, 10))

        output_container = tk.Frame(self.root, bg="#252d42", bd=0, relief="ridge")
        output_container.pack(padx=20, pady=5, fill="both", expand=False)

        tk.Label(
            output_container,
            text="Current Stack",
            font=("Segoe UI", 12, "underline"),
            bg="#252d42",
            fg="#ffffff"
        ).pack(pady=(10, 5))

        self.output = tk.Listbox(
            output_container,
            height=10,
            width=32,
            font=("Segoe UI", 11),
            activestyle="none",
            bg="#1f2938",
            fg="#e3e8ff",
            bd=0,
            highlightthickness=0,
            selectbackground="#4f5f8d",
            selectforeground="#ffffff"
        )
        self.output.pack(padx=10, pady=(0, 10))

        button_frame = tk.Frame(self.root, bg="#1f2533")
        button_frame.pack(pady=12)

        button_style = {
            "font": ("Segoe UI", 10, "bold"),
            "bg": "#3b76d7",
            "fg": "white",
            "activebackground": "#2b5bb3",
            "activeforeground": "white",
            "bd": 0,
            "width": 14,
            "height": 1
        }

        tk.Button(button_frame, text="Push", command=self.push, **button_style).grid(row=0, column=0, padx=6, pady=6)
        tk.Button(button_frame, text="Pop", command=self.pop_item, **button_style).grid(row=0, column=1, padx=6, pady=6)
        tk.Button(button_frame, text="Peek", command=self.peek, **button_style).grid(row=1, column=0, padx=6, pady=6)
        tk.Button(button_frame, text="Is Empty?", command=self.check_empty, **button_style).grid(row=1, column=1, padx=6, pady=6)
        tk.Button(button_frame, text="Size", command=self.show_size, **button_style).grid(row=2, column=0, padx=6, pady=6)
        tk.Button(button_frame, text="Refresh", command=self.refresh, **button_style).grid(row=2, column=1, padx=6, pady=6)

        tk.Button(
            self.root,
            text="Quit",
            command=self.root.destroy,
            font=("Segoe UI", 11, "bold"),
            bg="#d6455f",
            fg="white",
            activebackground="#a63348",
            activeforeground="white",
            bd=0,
            width=24,
            height=1
        ).pack(pady=16)

        self.refresh()

    def refresh(self):
        self.output.delete(0, tk.END)
        if self.stack.is_empty():
            self.output.insert(tk.END, "Stack is empty")
        else:
            for item in reversed(self.stack.items):
                self.output.insert(tk.END, item)
        top_item = self.stack.peek() if not self.stack.is_empty() else "None"
        self.status_label.config(text=f"Size: {self.stack.size()} | Top: {top_item}", fg="#a3d4ff")

    def push(self):
        value = self.entry.get().strip()
        if value == "":
            messagebox.showwarning("Warning", "Please enter an item to push.")
            return
        self.stack.push(value)
        self.entry.delete(0, tk.END)
        self.status_label.config(text=f"'{value}' has been pushed onto the stack", fg="#90ee90")
        self.refresh()

    def pop_item(self):
        try:
            value = self.stack.pop()
            self.status_label.config(text=f"'{value}' has been popped from the stack", fg="#ff9999")
            self.refresh()
        except IndexError as err:
            messagebox.showerror("Error", str(err))

    def peek(self):
        try:
            top = self.stack.peek()
            messagebox.showinfo("Top Item", f"Top item: {top}")
        except IndexError as err:
            messagebox.showerror("Error", str(err))

    def check_empty(self):
        message = "Yes" if self.stack.is_empty() else "No"
        messagebox.showinfo("Empty Check", f"Is the stack empty? {message}")

    def show_size(self):
        messagebox.showinfo("Stack Size", f"Size of the stack: {self.stack.size()}")


if __name__ == "__main__":
    root = tk.Tk()
    StackGUI(root)
    root.mainloop()
