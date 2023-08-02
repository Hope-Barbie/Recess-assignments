#CALCULATOR
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
window.title("BABIRYE HOPE'S CALCULATOR")

# Create the entry widget
entry = tk.Entry(window, width=40, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operators
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.','%', '+']
]
for i in range(4):
    for j in range(4):
        button = tk.Button(window, text=buttons[i][j], padx=30, pady=20,
                          command=lambda x=buttons[i][j]: button_click(x),
                          bg='white', fg='black') 
        button.grid(row=i+1, column=j, padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(window, text='Clear', padx=20, pady=10, command=button_clear,bg='red', fg='black')
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create the equal button
equal_button = tk.Button(window, text='=', padx=30, pady=20, command=button_equal,bg='grey', fg='black')
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

#Changing the background color 
window.configure(bg='orange')

# Run the main event loop
window.mainloop()