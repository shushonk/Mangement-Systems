import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Function to check if the inventory file exists
def check_inventory_file():
    if not os.path.exists('inventory.txt'):
        with open('inventory.txt', 'w'):  # Create an empty inventory file if it doesn't exist
            pass

# Function to add a new inventory entry
def add_inventory():
    item_name = item_name_entry.get().strip()
    item_qty = item_qty_entry.get().strip()

    if not item_name or not item_qty.isdigit():
        result_label.config(text="Invalid input! Please enter a valid item name and quantity.")
        return
    
    item_qty = int(item_qty)
    with open('inventory.txt', 'a') as file:
        file.write(f'{item_name},{item_qty}\n')
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    result_label.config(text=f"Added: {item_name} - {item_qty}")

# Function to update an existing inventory entry
def update_inventory():
    item_name = item_name_entry.get().strip()
    item_qty = item_qty_entry.get().strip()

    if not item_name or not item_qty.isdigit():
        result_label.config(text="Invalid input! Please enter a valid item name and quantity.")
        return
    
    item_qty = int(item_qty)
    updated = False
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty = line.strip().split(',')
            if name == item_name:
                file.write(f'{name},{item_qty}\n')
                updated = True
            else:
                file.write(line)
    
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    
    if updated:
        result_label.config(text=f"Updated: {item_name} - {item_qty}")
    else:
        result_label.config(text=f"{item_name} not found in inventory.")

# Function to search and display an inventory entry
def search_inventory():
    search_name = item_name_entry.get().strip()

    if not search_name:
        result_label.config(text="Please enter a valid item name.")
        return
    
    found = False
    with open('inventory.txt', 'r') as file:
        for line in file:
            name, qty = line.strip().split(',')
            if name == search_name:
                result_label.config(text=f'{name} - {qty}')
                found = True
                break
    if not found:
        result_label.config(text=f'{search_name} not found in inventory.')
    item_name_entry.delete(0, tk.END)

# Function to remove an existing inventory entry
def remove_inventory():
    remove_name = item_name_entry.get().strip()

    if not remove_name:
        result_label.config(text="Please enter a valid item name.")
        return
    
    removed = False
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty = line.strip().split(',')
            if name != remove_name:
                file.write(line)
            else:
                removed = True
    
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    
    if removed:
        result_label.config(text=f"Removed: {remove_name}")
    else:
        result_label.config(text=f"{remove_name} not found in inventory.")

# Function to generate a full list of inventory, formatted like a bill
def generate_inventory():
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    
    if inventory_data:
        # Create a nicely formatted inventory report
        inventory_text = "========================================\n"
        inventory_text += f"         Inventory Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        inventory_text += "========================================\n"
        inventory_text += "{:<20} {:<10}\n".format("Item Name", "Quantity")  # Header row
        inventory_text += "----------------------------------------\n"
        
        for line in inventory_data:
            name, qty = line.strip().split(',')
            inventory_text += "{:<20} {:<10}\n".format(name, qty)  # Formatting each row

        inventory_text += "========================================\n"
        result_label.config(text=inventory_text)
    else:
        result_label.config(text="Inventory is empty.")

# Create the main window
root = tk.Tk()
root.title("Inventory Management")
root.geometry("600x400")
root.configure(bg="#f0f0f0")  # Set a light background color

# Check if the inventory file exists
check_inventory_file()

# Input fields with placeholder text
item_name_label = tk.Label(root, text="Item Name:", font=("Arial", 12), bg="#f0f0f0")
item_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
item_name_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=2, relief="solid")
item_name_entry.grid(row=0, column=1, padx=10, pady=10)
item_name_entry.insert(0, "Enter item name...")  # Placeholder text

item_qty_label = tk.Label(root, text="Item Quantity:", font=("Arial", 12), bg="#f0f0f0")
item_qty_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
item_qty_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=2, relief="solid")
item_qty_entry.grid(row=1, column=1, padx=10, pady=10)
item_qty_entry.insert(0, "Enter quantity...")  # Placeholder text

# Button Style (modern and clean)
button_style = {'font': ("Arial", 12), 'bg': "#4CAF50", 'fg': "white", 'width': 15, 'height': 2, 'relief': "solid"}

# Buttons
add_button = tk.Button(root, text="Add Inventory", command=add_inventory, **button_style)
add_button.grid(row=2, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Inventory", command=update_inventory, **button_style)
update_button.grid(row=2, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search Inventory", command=search_inventory, **button_style)
search_button.grid(row=3, column=0, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Inventory", command=remove_inventory, **button_style)
remove_button.grid(row=3, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Inventory", command=generate_inventory, **button_style)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Result Label (styled to look clean)
result_label = tk.Label(root, text="List", font=("Arial", 12), bg="#f0f0f0", fg="blue", justify=tk.LEFT)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Tooltips for guidance
def on_add_button_hover(event):
    result_label.config(text="Click to add a new item to inventory.")

def on_update_button_hover(event):
    result_label.config(text="Click to update the quantity of an existing item.")

def on_search_button_hover(event):
    result_label.config(text="Search for an item by name.")

def on_remove_button_hover(event):
    result_label.config(text="Remove an item from inventory.")

def on_generate_button_hover(event):
    result_label.config(text="Generate and view the full inventory list.")

add_button.bind("<Enter>", on_add_button_hover)
update_button.bind("<Enter>", on_update_button_hover)
search_button.bind("<Enter>", on_search_button_hover)
remove_button.bind("<Enter>", on_remove_button_hover)
generate_button.bind("<Enter>", on_generate_button_hover)

# Run the application
root.mainloop()
