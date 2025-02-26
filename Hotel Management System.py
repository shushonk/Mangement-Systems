import tkinter as tk
from tkinter import messagebox
import mysql.connector

# GLOBAL VARIABLES
mycon = None
cursor = None
userName = ""
password = ""
room_rent = 0
restaurant_bill = 0
totalAmount = 0
cid = ""

# MODULE TO CHECK MYSQL CONNECTION
def MYSQLconnectionCheck():
    global mycon
    global userName
    global password
    userName = entry_username.get()
    password = entry_password.get()
    try:
        mycon = mysql.connector.connect(
            host="localhost", 
            user=userName, 
            passwd=password, 
            auth_plugin='mysql_native_password'
        )
        if mycon:
            messagebox.showinfo("Success", "MySQL Connection Established Successfully!")
            cursor = mycon.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
            cursor.execute("COMMIT")
            cursor.close()
        return mycon
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# MODULE TO CONNECT TO DATABASE
def MYSQLconnection():
    global mycon
    try:
        mycon = mysql.connector.connect(
            host="localhost", 
            user=userName, 
            passwd=password, 
            database="HMS", 
            auth_plugin='mysql_native_password'
        )
        if mycon:
            print('Connected to "HMS" database.')
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        mycon.close()

# Guest details form
def guest_details():
    global cid
    try:
        cursor = mycon.cursor()
        create_table = """CREATE TABLE IF NOT EXISTS C_DETAILS(
                          CID VARCHAR(20), C_NAME VARCHAR(30), C_ADDRESS VARCHAR(30),
                          C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30), P_NO VARCHAR(30), C_EMAIL VARCHAR(30))"""
        cursor.execute(create_table)
        cursor.close()

        cid = entry_cid.get()
        name = entry_name.get()
        address = entry_address.get()
        age = entry_age.get()
        country = entry_country.get()
        phone_no = entry_phone.get()
        email = entry_email.get()

        sql = "INSERT INTO C_DETAILS VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values = (cid, name, address, age, country, phone_no, email)

        cursor = mycon.cursor()
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()

        messagebox.showinfo("Success", "New Guest Registered Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Booking Form
def booking():
    try:
        cursor = mycon.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20), CHECK_IN DATE, CHECK_OUT DATE)"
        cursor.execute(create_table)
        cursor.close()

        checkin = entry_checkin.get()
        checkout = entry_checkout.get()

        sql = "INSERT INTO BOOKING_RECORD VALUES(%s, %s, %s)"
        values = (cid, checkin, checkout)

        cursor = mycon.cursor()
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()

        messagebox.showinfo("Success", "Booking Details Added Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Calculate Room Rent
def room_rent_calculation():
    global room_rent
    try:
        room_choice = int(entry_room_choice.get())
        room_no = int(entry_room_no.get())
        no_of_days = int(entry_no_of_days.get())

        if room_choice == 1:
            room_rent = no_of_days * 10000
        elif room_choice == 2:
            room_rent = no_of_days * 5000
        elif room_choice == 3:
            room_rent = no_of_days * 3500
        elif room_choice == 4:
            room_rent = no_of_days * 2500
        else:
            messagebox.showerror("Error", "Invalid Room Choice!")
            return

        messagebox.showinfo("Room Rent", f"Your Room Rent for {no_of_days} days is: {room_rent} INR")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Calculate Restaurant Bill
def restaurant_bill_calculation():
    global restaurant_bill
    try:
        choice_dish = int(entry_dish_choice.get())
        quantity = int(entry_quantity.get())

        if choice_dish == 1:
            restaurant_bill = quantity * 300
        elif choice_dish == 2:
            restaurant_bill = quantity * 500
        elif choice_dish == 3:
            restaurant_bill = quantity * 750
        else:
            messagebox.showerror("Error", "Invalid Dish Choice!")
            return

        messagebox.showinfo("Restaurant Bill", f"Your Total Restaurant Bill is: {restaurant_bill} INR")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Calculate Total Amount
def total_amount():
    global room_rent, restaurant_bill
    try:
        grand_total = room_rent + restaurant_bill
        messagebox.showinfo("Total Amount", f"Total Amount to be Paid: {grand_total} INR")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main Window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("600x600")  # Set window size to 600x600

# MySQL Username and Password Section
frame_mysql = tk.Frame(root)
frame_mysql.pack(padx=10, pady=10)

tk.Label(frame_mysql, text="Enter MySQL Username:").grid(row=0, column=0, sticky="e")
entry_username = tk.Entry(frame_mysql)
entry_username.grid(row=0, column=1)

tk.Label(frame_mysql, text="Enter MySQL Password:").grid(row=1, column=0, sticky="e")
entry_password = tk.Entry(frame_mysql, show="*")  # Password field will hide input text
entry_password.grid(row=1, column=1)

tk.Button(frame_mysql, text="Connect to MySQL", command=MYSQLconnectionCheck).grid(row=2, columnspan=2, pady=5)

# Guest Registration Section
frame_guest = tk.Frame(root)
frame_guest.pack(padx=10, pady=10)

tk.Label(frame_guest, text="Guest ID:").grid(row=0, column=0, sticky="e")
entry_cid = tk.Entry(frame_guest)
entry_cid.grid(row=0, column=1)

tk.Label(frame_guest, text="Name:").grid(row=1, column=0, sticky="e")
entry_name = tk.Entry(frame_guest)
entry_name.grid(row=1, column=1)

tk.Label(frame_guest, text="Address:").grid(row=2, column=0, sticky="e")
entry_address = tk.Entry(frame_guest)
entry_address.grid(row=2, column=1)

tk.Label(frame_guest, text="Age:").grid(row=3, column=0, sticky="e")
entry_age = tk.Entry(frame_guest)
entry_age.grid(row=3, column=1)

tk.Label(frame_guest, text="Country:").grid(row=4, column=0, sticky="e")
entry_country = tk.Entry(frame_guest)
entry_country.grid(row=4, column=1)

tk.Label(frame_guest, text="Phone No:").grid(row=5, column=0, sticky="e")
entry_phone = tk.Entry(frame_guest)
entry_phone.grid(row=5, column=1)

tk.Label(frame_guest, text="Email:").grid(row=6, column=0, sticky="e")
entry_email = tk.Entry(frame_guest)
entry_email.grid(row=6, column=1)

tk.Button(frame_guest, text="Register Guest", command=guest_details).grid(row=7, columnspan=2, pady=5)

# Booking Section
frame_booking = tk.Frame(root)
frame_booking.pack(padx=10, pady=10)

tk.Label(frame_booking, text="Check-in Date [YYYY-MM-DD]:").grid(row=0, column=0, sticky="e")
entry_checkin = tk.Entry(frame_booking)
entry_checkin.grid(row=0, column=1)

tk.Label(frame_booking, text="Check-out Date [YYYY-MM-DD]:").grid(row=1, column=0, sticky="e")
entry_checkout = tk.Entry(frame_booking)
entry_checkout.grid(row=1, column=1)

tk.Button(frame_booking, text="Book Room", command=booking).grid(row=2, columnspan=2, pady=5)

# Room Rent Section
frame_room_rent = tk.Frame(root)
frame_room_rent.pack(padx=10, pady=10)

tk.Label(frame_room_rent, text="Room Choice (1-4):").grid(row=0, column=0, sticky="e")
entry_room_choice = tk.Entry(frame_room_rent)
entry_room_choice.grid(row=0, column=1)

tk.Label(frame_room_rent, text="Room No:").grid(row=1, column=0, sticky="e")
entry_room_no = tk.Entry(frame_room_rent)
entry_room_no.grid(row=1, column=1)

tk.Label(frame_room_rent, text="No. of Days:").grid(row=2, column=0, sticky="e")
entry_no_of_days = tk.Entry(frame_room_rent)
entry_no_of_days.grid(row=2, column=1)

tk.Button(frame_room_rent, text="Calculate Room Rent", command=room_rent_calculation).grid(row=3, columnspan=2, pady=5)

# Restaurant Bill Section
frame_restaurant = tk.Frame(root)
frame_restaurant.pack(padx=10, pady=10)

tk.Label(frame_restaurant, text="Dish Choice (1-3):").grid(row=0, column=0, sticky="e")
entry_dish_choice = tk.Entry(frame_restaurant)
entry_dish_choice.grid(row=0, column=1)

tk.Label(frame_restaurant, text="Quantity:").grid(row=1, column=0, sticky="e")
entry_quantity = tk.Entry(frame_restaurant)
entry_quantity.grid(row=1, column=1)

tk.Button(frame_restaurant, text="Calculate Restaurant Bill", command=restaurant_bill_calculation).grid(row=2, columnspan=2, pady=5)

# Total Amount Section
tk.Button(root, text="Generate Total Bill", command=total_amount).pack(pady=10)

root.mainloop()
