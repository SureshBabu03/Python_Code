import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display input and results
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons
row_val = 1
col_val = 0
buttons = []
for label in button_labels:
    if label == '=':
        button = tk.Button(window, text=label, width=5, command=calculate)
    elif label == 'C':
        button = tk.Button(window, text=label, width=5, command=lambda: entry.delete(0, tk.END))
    else:
        button = tk.Button(window, text=label, width=5, command=lambda label=label: button_click(label))
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
    buttons.append(button)

# Start the GUI event loop
window.mainloop()
