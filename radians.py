import tkinter as tk
from tkinter import messagebox
import math
import re

# Default mode is Degrees
is_degrees = True

def toggle_mode():
    """Switch between Degrees and Radians mode"""
    global is_degrees
    is_degrees = not is_degrees  # Toggle mode
    mode_label.config(text=f"Mode: {'Degrees' if is_degrees else 'Radians'}")  # Update label

def evaluate_expression(expression):
    """Evaluate mathematical expressions with trigonometric functions"""
    try:
        global is_degrees

        # Adjust trigonometric functions based on mode
        if is_degrees:
            expression = re.sub(r"sin\(([^)]+)\)", r"math.sin(math.radians(\1))", expression)
            expression = re.sub(r"cos\(([^)]+)\)", r"math.cos(math.radians(\1))", expression)
            expression = re.sub(r"tan\(([^)]+)\)", r"math.tan(math.radians(\1))", expression)
        else:
            expression = re.sub(r"sin\(([^)]+)\)", r"math.sin(\1)", expression)
            expression = re.sub(r"cos\(([^)]+)\)", r"math.cos(\1)", expression)
            expression = re.sub(r"tan\(([^)]+)\)", r"math.tan(\1)", expression)

        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return result

    except Exception as e:
        return f"Error: {e}"

def calculate():
    """Handle calculation and display result"""
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
    """Insert numbers or symbols into entry field"""
    entry.insert(tk.END, value)

def clear():
    """Clear the entry field"""
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")

# Display mode label
mode_label = tk.Label(root, text="Mode: Degrees", font=("Arial", 12))
mode_label.grid(row=0, column=0, columnspan=4, pady=5)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
    ('C', 6, 0), ('sin(', 6, 1), ('cos(', 6, 2), ('tan(', 6, 3),
    ('(', 7, 0), (')', 7, 1), ('Toggle Mode', 7, 2)  # Toggle button for Degrees/Radians
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=10, height=2, command=clear)
    elif text == "Toggle Mode":
        btn = tk.Button(root, text=text, width=20, height=2, command=toggle_mode)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_value(t))

    btn.grid(row=row, column=col, padx=5, pady=5, columnspan=(2 if text == "Toggle Mode" else 1))

root.mainloop()
