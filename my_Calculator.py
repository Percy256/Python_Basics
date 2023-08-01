
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Ssemaganda_Trevour_calculator")

# Create an entry widget to display the calculator input and output
entry = tk.Entry(window, width=30, font=('Arial', 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button style
button_style = {'font': ('Arial', 12), 'width': 5, 'height': 2}

# Create buttons for numbers 0-9
for i in range(9):
    button = tk.Button(window, text=str(i+1), **button_style, command=lambda i=i: button_click(i+1))
    button.grid(row=1+(i//3), column=i%3, padx=5, pady=5)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, **button_style, command=lambda operator=operator: button_click(operator))
    button.grid(row=i+2, column=3, padx=5, pady=5)

# Create additional buttons for 0, clear, and equals
button_0 = tk.Button(window, text='0', **button_style, command=lambda: button_click(0))
button_clear = tk.Button(window, text='C', **button_style, command=button_clear)
button_equal = tk.Button(window, text='=', **button_style, command=button_equal)

button_0.grid(row=4, column=0, padx=5, pady=5)
button_clear.grid(row=4, column=1, padx=5, pady=5)
button_equal.grid(row=4, column=2, padx=5, pady=5)

# Configure grid weights to make buttons expandable
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

# Start the main event loop
window.mainloop()