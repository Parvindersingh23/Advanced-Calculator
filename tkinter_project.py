import tkinter as tk
from tkinter import messagebox
import math

def on_click(event):
    widget = event.widget
    widget.config(bg='lightgray')

def on_release(event):
    widget = event.widget
    widget.config(bg='#4682B4')

def click_button(value):
    try:
        if value == "C":
            entry.delete(0, tk.END)
        elif value == "=":
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value in ("sin", "cos", "tan", "log", "sqrt"):
            expression = entry.get()
            if value == "sin":
                result = math.sin(math.radians(float(expression)))
            elif value == "cos":
                result = math.cos(math.radians(float(expression)))
            elif value == "tan":
                result = math.tan(math.radians(float(expression)))
            elif value == "log":
                result = math.log(float(expression))
            elif value == "sqrt":
                result = math.sqrt(float(expression))

            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            entry.insert(tk.END, value)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg='#2F4F4F')

entry = tk.Entry(root, font=("Arial", 20), bg="#F0F8FF", fg="#000000", borderwidth=2, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("tan", 5, 3),
    ("log", 6, 0), ("sqrt", 6, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18, "bold"), bg="#4682B4", fg="white", relief=tk.RAISED, activebackground="#B0C4DE", activeforeground="black")
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Enter>", on_click)
    button.bind("<Leave>", on_release)
    button.config(command=lambda t=text: click_button(t))

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()