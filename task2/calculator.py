import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create a window
window = tk.Tk()
window.title("Calculator")

# Create an output/display window
display = tk.Entry(window, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

# Define buttons for numbers 0-9 and arithmetic operations
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for text, row, col in button_texts:
    button = tk.Button(window, text=text, padx=20, pady=10)
    if text == '=':
        button.config(command=button_equal)
    elif text == 'C':
        button.config(command=button_clear)
    else:
        button.config(command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Run the main event loop
window.mainloop()
