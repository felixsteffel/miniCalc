import tkinter as tk

# -------------------------------------------------
# Logik
# -------------------------------------------------

def append_digit(d):
    expression_var.set(expression_var.get() + d)

def set_operator(op):
    expr = expression_var.get()
    if expr and expr[-1] not in "+-*/":
        expression_var.set(expr + op)

def backspace():
    expression_var.set(expression_var.get()[:-1])
    result_var.set("")

def clear_all():
    expression_var.set("")
    result_var.set("")

def calculate():
    expr = expression_var.get()
    try:
        if not expr or expr[-1] in "+-*/":
            return
        result = eval(expr)
        expression_var.set(expr + "=")
        result_var.set(str(result))
    except Exception:
        result_var.set("Fehler")

# -------------------------------------------------
# Fenster
# -------------------------------------------------

root = tk.Tk()
root.title("Mini-Rechner")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# -------------------------------------------------
# Display
# -------------------------------------------------

expression_var = tk.StringVar()
result_var = tk.StringVar()

display_frame = tk.Frame(root, bg="#2b2b2b", bd=2, relief="ridge")
display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

expr_label = tk.Label(
    display_frame,
    textvariable=expression_var,
    anchor="w",
    bg="#2b2b2b",
    fg="#cccccc",
    font=("Consolas", 14)
)
expr_label.pack(fill="x", padx=8, pady=(5, 0))

result_label = tk.Label(
    display_frame,
    textvariable=result_var,
    anchor="e",
    bg="#2b2b2b",
    fg="#ffffff",
    font=("Consolas", 20, "bold")
)
result_label.pack(fill="x", padx=8, pady=(0, 5))

# -------------------------------------------------
# Buttons
# -------------------------------------------------

buttons = [
    ('7', 'digit'), ('8', 'digit'), ('9', 'digit'), ('⌫', 'back'),
    ('4', 'digit'), ('5', 'digit'), ('6', 'digit'), ('/', 'op'),
    ('1', 'digit'), ('2', 'digit'), ('3', 'digit'), ('*', 'op'),
    ('0', 'digit'), ('.', 'digit'), ('=', 'eq'), ('+', 'op'),
]

row, col = 1, 0

for text, kind in buttons:
    if kind == 'digit':
        cmd = lambda t=text: append_digit(t)
    elif kind == 'op':
        cmd = lambda t=text: set_operator(t)
    elif kind == 'back':
        cmd = backspace
    elif kind == 'eq':
        cmd = calculate
    else:
        cmd = lambda: None

    tk.Button(
        root,
        text=text,
        command=cmd,
        width=5,
        height=2,
        font=("Arial", 12),
        bg="#3a3a3a",
        fg="white",
        activebackground="#505050",
        activeforeground="white",
        bd=0
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear Button
tk.Button(
    root,
    text="C",
    command=clear_all,
    width=22,
    height=2,
    font=("Arial", 12),
    bg="#8b0000",
    fg="white",
    activebackground="#a40000",
    bd=0
).grid(row=row, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
