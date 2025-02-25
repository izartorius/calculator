import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression), {"_builtins_":None},math._dict_)
        entry.delete(0, tk.END)
        entry.insert(tk.END), str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")

