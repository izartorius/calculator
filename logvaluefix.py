import tkinter as tk
from tkinter import messagebox
import math
import re  # Import regex module

def evaluate_expression(expression):
    try:
        # Handling logarithms manually
        # Convert log(x, y) -> math.log(x, y)
        expression = re.sub(r"log\(\s*([\d.]+)\s*,\s*([\d.]+)\s*\)", r"math.log(\1, \2)", expression)

        # Convert log(x) -> math.log(x, 10) if base is missing
        expression = re.sub(r"log\(\s*([\d.]+)\s*\)", r"math.log(\1, 10)", expression)

        # Evaluate expression safely using math functions
        result = eval(expression, {"__builtins__": None}, math.__dict__)

        return result

    except Exception as e:
        return f"Error: {e}"

def calculate():
    try:
        expression = entry.get().strip()

        if not expression:
            raise ValueError("Empty expression")

        result = evaluate_expression(expression)

        if isinstance(result, str) and result.startswith("Error"):
            messagebox.showerror("Error", result)
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")

def insert_value(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('log(', 5, 1), ('(', 5, 2), (')', 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=10, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_value(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
