import tkinter as tk
from tkinter import messagebox
import math

# Default mode is Degrees
is_degrees = True

def toggle_mode():
    """Switch between Degrees and Radians mode"""
    global is_degrees
    is_degrees = not is_degrees  # Toggle mode
    mode_label.config(text=f"Mode: {'Degrees' if is_degrees else 'Radians'}")  # Update label

def evaluate_expression(expression):
    """Evaluate mathematical expressions with trigonometric functions and logarithms"""
    try:
        global is_degrees

        # Convert trigonometric functions based on mode
        if is_degrees:
            expression = expression.replace("sin(", "math.sin(math.radians(")
            expression = expression.replace("cos(", "math.cos(math.radians(")
            expression = expression.replace("tan(", "math.tan(math.radians(")
        else:
            expression = expression.replace("sin(", "math.sin(")
            expression = expression.replace("cos(", "math.cos(")
            expression = expression.replace("tan(", "math.tan(")

        # Handle logarithm manually
        while "log(" in expression:
            start = expression.find("log(")
            end = expression.find(")", start)
            if end == -1:
                raise ValueError("Unmatched parentheses in log function")

            log_content = expression[start + 4:end]  # Extract inside of log()
            parts = log_content.split(",")  # Check if base is provided
            if len(parts) == 1:
                log_result = math.log10(float(parts[0]))  # Default base 10
            elif len(parts) == 2:
                log_result = math.log(float(parts[0]), float(parts[1]))  # Custom base
            else:
                raise ValueError("Invalid log format. Use log(value) or log(value, base)")

            expression = expression[:start] + str(log_result) + expression[end + 1:]

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
    ('(', 7, 0), (')', 7, 1), ('log(', 7, 2), ('Toggle Mode', 7, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=10, height=2, command=clear)
    elif text == "Toggle Mode":
        btn = tk.Button(root, text=text, width=15, height=2, command=toggle_mode)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_value(t))

    btn.grid(row=row, column=col, padx=5, pady=5, columnspan=(2 if text == "Toggle Mode" else 1))

root.mainloop()
