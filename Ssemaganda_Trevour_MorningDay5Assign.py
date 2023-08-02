import tkinter as tk

def print_receipt():
    # Gather receipt details from user inputs
    customer_name = customer_name_entry.get()
    items = items_text.get("1.0", tk.END)
    total_amount = total_amount_entry.get()

    # Create the receipt string
    receipt = "-------------------------\n"
    receipt += "      RECEIPT\n"
    receipt += "-------------------------\n\n"
    receipt += "Customer: {}\n\n".format(customer_name)
    receipt += "Items:\n"
    receipt += items + "\n"
    receipt += "Total Amount: ${}\n".format(total_amount)
    receipt += "-------------------------"

    # Create a new window to display the receipt
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")

    receipt_label = tk.Label(receipt_window, text=receipt, font=("Arial", 12))
    receipt_label.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Receipt Printer")

# Create and pack a label and entry for customer name
customer_name_label = tk.Label(root, text="Customer Name:")
customer_name_label.pack(padx=10, pady=5)

customer_name_entry = tk.Entry(root)
customer_name_entry.pack(padx=10, pady=5)

# Create and pack a label and text widget for items
items_label = tk.Label(root, text="Items:")
items_label.pack(padx=10, pady=5)

items_text = tk.Text(root, height=5, width=30)
items_text.pack(padx=10, pady=5)

# Create and pack a label and entry for total amount
total_amount_label = tk.Label(root, text="Total Amount:")
total_amount_label.pack(padx=10, pady=5)

total_amount_entry = tk.Entry(root)
total_amount_entry.pack(padx=10, pady=5)

# Create and pack the Print Receipt button
print_button = tk.Button(root, text="Print Receipt", command=print_receipt)
print_button.pack(padx=10, pady=10)

root.mainloop()
