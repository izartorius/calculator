import tkinter as tk
from tkinter import messagebox
import math


def calculate():
    try:
        expression = entry.get()
        result = eval(expression, {"_builtins_": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")



def insert_value(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.GROOVE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('sin', 'cos', 'tan', 'log'),
    ('sqrt', 'exp', '(', ')'),
    ('C',)
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for char in row:
        if char == '=':
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=calculate)
        elif char == "C":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=clear)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18),
                            command=lambda ch=char: insert_value(ch))
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()