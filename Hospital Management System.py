import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Hospital:
    def __init__(self):
        self.sno = 0
        self.name = ''
        self.age = 0
        self.sex = ""
        self.email = ""
        self.fname = ""
        self.address = ''
        self.city = ''
        self.state = ''
        self.height = 0
        self.weight = 0
        self.doctor = ''
        self.med = ''
        self.bill = 0
        self.paymethod = ''
        self.pno = 0
        self.bgroup = ''
        self.dname = ''

    def input_data(self, sno, name, age, sex, height, weight, bgroup, fname, address, city, state, pno, email, doctor, dname, med, bill, paymethod):
        self.sno = sno
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.bgroup = bgroup
        self.fname = fname
        self.address = address
        self.city = city
        self.state = state
        self.pno = pno
        self.email = email
        self.doctor = doctor
        self.dname = dname
        self.med = med
        self.bill = bill
        self.paymethod = paymethod

    def output_data(self):
        return f"Serial No: {self.sno}\nName: {self.name}\nAge: {self.age} | Sex: {self.sex}\nHeight: {self.height} cm | Weight: {self.weight} kg\n" \
               f"Blood Group: {self.bgroup}\nFather's Name: {self.fname}\nAddress: {self.address}, {self.city}, {self.state}\n" \
               f"Phone: {self.pno} | Email: {self.email}\nDoctor: {self.doctor}\nDisease: {self.dname}\nMedicine: {self.med}\n" \
               f"Bill: ${self.bill:.2f} | Payment: {self.paymethod}\n" \
               "------------------------------------------------------------"


def write_hospital():
    # Check for empty fields and handle conversion errors
    try:
        sno = entry_sno.get()
        if sno == '':
            raise ValueError("Serial No cannot be empty.")
        sno = int(sno)

        name = entry_name.get()
        age = entry_age.get()
        if age == '':
            raise ValueError("Age cannot be empty.")
        age = int(age)

        sex = entry_sex.get()
        height = entry_height.get()
        if height == '':
            raise ValueError("Height cannot be empty.")
        height = float(height)

        weight = entry_weight.get()
        if weight == '':
            raise ValueError("Weight cannot be empty.")
        weight = float(weight)

        bgroup = entry_bgroup.get()
        fname = entry_fname.get()
        address = entry_address.get()
        city = entry_city.get()
        state = entry_state.get()

        pno = entry_pno.get()
        if pno == '':
            raise ValueError("Phone number cannot be empty.")
        pno = int(pno)

        email = entry_email.get()
        doctor = entry_doctor.get()
        dname = entry_dname.get()
        med = entry_med.get()

        bill = entry_bill.get()
        if bill == '':
            raise ValueError("Bill amount cannot be empty.")
        # Remove dollar sign and convert to float
        bill = float(bill.replace('$', '').strip())

        paymethod = entry_paymethod.get()

        # Now, create a Hospital object and save it
        hospital = Hospital()
        hospital.input_data(sno, name, age, sex, height, weight, bgroup, fname, address, city, state, pno, email, doctor, dname, med, bill, paymethod)

        # Save the hospital record to the file
        with open("Hospital1.DAT", "ab") as fout:
            pickle.dump(hospital, fout)

        messagebox.showinfo("Success", "Record Saved Successfully!")
        display_saved_record(hospital)  # Display the saved record immediately
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


def read_hospital():
    text_output.delete(1.0, tk.END)
    try:
        with open("Hospital1.DAT", "rb") as fin:
            while True:
                hospital = pickle.load(fin)
                text_output.insert(tk.END, hospital.output_data() + "\n\n")
    except EOFError:
        pass


def display_saved_record(hospital):
    # Display the record immediately after saving
    text_output.insert(tk.END, hospital.output_data() + "\n\n")


# Main window
root = tk.Tk()
root.title("Hospital Management System")

# Input fields
label_sno = tk.Label(root, text="Serial No")
label_sno.grid(row=0, column=0)
entry_sno = tk.Entry(root)
entry_sno.grid(row=0, column=1)

label_name = tk.Label(root, text="Name")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

label_age = tk.Label(root, text="Age")
label_age.grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

label_sex = tk.Label(root, text="Sex")
label_sex.grid(row=3, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=3, column=1)

label_height = tk.Label(root, text="Height")
label_height.grid(row=4, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=4, column=1)

label_weight = tk.Label(root, text="Weight")
label_weight.grid(row=5, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=5, column=1)

label_bgroup = tk.Label(root, text="Blood Group")
label_bgroup.grid(row=6, column=0)
entry_bgroup = tk.Entry(root)
entry_bgroup.grid(row=6, column=1)

label_fname = tk.Label(root, text="Father's Name")
label_fname.grid(row=7, column=0)
entry_fname = tk.Entry(root)
entry_fname.grid(row=7, column=1)

label_address = tk.Label(root, text="Address")
label_address.grid(row=8, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=8, column=1)

label_city = tk.Label(root, text="City")
label_city.grid(row=9, column=0)
entry_city = tk.Entry(root)
entry_city.grid(row=9, column=1)

label_state = tk.Label(root, text="State")
label_state.grid(row=10, column=0)
entry_state = tk.Entry(root)
entry_state.grid(row=10, column=1)

label_pno = tk.Label(root, text="Phone No")
label_pno.grid(row=11, column=0)
entry_pno = tk.Entry(root)
entry_pno.grid(row=11, column=1)

label_email = tk.Label(root, text="Email")
label_email.grid(row=12, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=12, column=1)

label_doctor = tk.Label(root, text="Doctor's Name")
label_doctor.grid(row=13, column=0)
entry_doctor = tk.Entry(root)
entry_doctor.grid(row=13, column=1)

label_dname = tk.Label(root, text="Disease Name")
label_dname.grid(row=14, column=0)
entry_dname = tk.Entry(root)
entry_dname.grid(row=14, column=1)

label_med = tk.Label(root, text="Medicine")
label_med.grid(row=15, column=0)
entry_med = tk.Entry(root)
entry_med.grid(row=15, column=1)

label_bill = tk.Label(root, text="Bill Amount")
label_bill.grid(row=16, column=0)
entry_bill = tk.Entry(root)
entry_bill.grid(row=16, column=1)

label_paymethod = tk.Label(root, text="Payment Method")
label_paymethod.grid(row=17, column=0)
entry_paymethod = tk.Entry(root)
entry_paymethod.grid(row=17, column=1)

# Buttons
button_save = tk.Button(root, text="Save Record", command=write_hospital)
button_save.grid(row=18, column=0, columnspan=2)

button_show_all = tk.Button(root, text="Show All Records", command=read_hospital)
button_show_all.grid(row=19, column=0, columnspan=2)

# Text widget for displaying records
text_output = tk.Text(root, width=100, height=15)
text_output.grid(row=20, column=0, columnspan=2)

root.mainloop()
