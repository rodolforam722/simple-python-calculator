import tkinter as tk
from tkinter import messagebox

# Operation functions
def agregar(valor):
    display.insert(tk.END, valor)

def limpiar():
    display.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Invalid expression")

# Window setup
root = tk.Tk()
root.title("Simple Python Calculator")

# Entry widget to display the expression/result
display = tk.Entry(
    root,
    font=("Arial", 24),
    borderwidth=2,
    relief="ridge",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Buttons layout: (label, row, column)
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in botones:
    if text == '=':
        # “=” button triggers the calculation
        btn = tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            font=("Arial", 18),
            command=calcular
        )
    else:
        # Digit or operator buttons append their label to the display
        btn = tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            font=("Arial", 18),
            command=lambda t=text: agregar(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button spans full width at bottom
limpiar_btn = tk.Button(
    root,
    text='C',
    width=5,
    height=2,
    font=("Arial", 18),
    command=limpiar
)
limpiar_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

# Run the application
root.mainloop()
