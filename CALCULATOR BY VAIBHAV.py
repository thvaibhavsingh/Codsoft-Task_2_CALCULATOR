import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Creating the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields for numbers
tk.Label(window, text="Enter first number:").grid(row=0, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)

tk.Label(window, text="Enter second number:").grid(row=1, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)

# Dropdown menu for selecting operation
tk.Label(window, text="Select operation:").grid(row=2, column=0)
operation_var = tk.StringVar(window)
operation_var.set("+")  # default value
operation_menu = tk.OptionMenu(window, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

# Button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, columnspan=2)

# Start the GUI event loop
window.mainloop()
