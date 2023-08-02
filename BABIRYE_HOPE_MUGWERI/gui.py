
import tkinter as tk

def print_receipt():
    # Code for printing the receipt
    receipt = f"BARBIE MINI SUPER MARKET\nKIKUMI KIKUMI BRANCH\n\nCustomer Name: {customer_entry.get()}\nItem: {item_entry.get()}\nQuantity: {quantity_entry.get()}\nPrice: {price_entry.get()}\nTotal: {total_entry.get()}\nTHANK YOU FOR SHOPPING WITH US"
    receipt_text.delete('1.0', tk.END)
    receipt_text.insert(tk.END, receipt)


window = tk.Tk()
window.title("Barbie Mini Super Market")

#labels and entry fields for inputs
customer_label = tk.Label(window, text="Customer Name:")
customer_label.pack()
customer_entry = tk.Entry(window)
customer_entry.pack()

item_label = tk.Label(window, text="Item:")
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

total_label = tk.Label(window, text="Total:")
total_label.pack()
total_entry = tk.Entry(window)
total_entry.pack()



# Create the print receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()


receipt_text = tk.Text(window, height=20, width=40, bg = "lightblue")
receipt_text.pack()


window.configure(bg='lightblue')

window.mainloop()

