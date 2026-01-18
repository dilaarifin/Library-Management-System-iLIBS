import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# DEFINITIONS
def back():
    window.destroy()
    import loginmember

def pay():
    import payment10

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY AUTOINCREMENT, member_name TEXT, member_address TEXT, member_birth TEXT, member_age INTEGER, member_race TEXT, member_religion TEXT, member_email TEXT, member_phone TEXT, member_user TEXT, member_date TEXT, member_pass TEXT)")
    conn.commit()
    conn.close()
    
def insert_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        member_name = entry_fullname.get()
        member_address = entry_address.get()
        member_birth = entry_birth.get()
        member_age = entry_age.get()
        member_race = entry_race.get()
        member_religion = entry_religion.get()
        member_email = entry_email.get()
        member_phone = entry_phone.get()
        member_date = entry_date.get()
        member_user = entry_username.get()
        member_pass = entry_password.get()
        
        if member_name and member_address and member_birth and member_age and member_race and member_religion and member_email and member_phone and member_date and member_user and member_pass:
        
            conn = sqlite3.connect("database.db") 
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members (member_name,member_address,member_birth,member_age,member_race,member_religion,member_email,member_phone,member_date,member_user,member_pass) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(member_name,member_address,member_birth,member_age,member_race,member_religion,member_email,member_phone,member_date,member_user,member_pass))    
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully added to database",icon='info')
        
            entry_fullname.delete(0,tk.END)
            entry_address.delete(0,tk.END)
            entry_birth.delete(0,tk.END)
            entry_age.delete(0,tk.END)
            entry_race.delete(0,tk.END)
            entry_religion.delete(0,tk.END)
            entry_email.delete(0,tk.END)
            entry_phone.delete(0,tk.END)
            entry_date.delete(0,tk.END)
            entry_username.delete(0,tk.END)
            entry_password.delete(0,tk.END)  
        else:
            tkinter.messagebox.showwarning(title="Error", message="Fields cannot be empty", icon="warning")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms", icon="warning")   

        
# Main Window        
window = tk.Tk()
window.title("Welcome to iLIBS: Sign Up User/Membership")
window.geometry("1000x600")
window.iconbitmap("icons/library.ico")
window.resizable(False,False)
window.configure(bg="#FF6A6A")

# Set the window size
window_width = 1000
window_height = 600

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main Frame
frame = tkinter.Frame(window, bg="#FF6A6A")
frame.pack()

home_buttom = tkinter.Button(frame, text="HOME",command=back)
home_buttom.grid(row=0,column=1,sticky="E")

lbl1 = tkinter.Label(frame, text="MEMBERSHIP REGISTRATION", font=("Arial", 30, "bold"), bg="#FF6A6A")
lbl1.grid(row=0,column=0,padx=10,pady=10)

# Registration/Payment Frame
membership_frame = tkinter.LabelFrame(frame, text="Registration")
membership_frame.grid(row=1,column=0, sticky="news", padx=20,pady=20)

lbl_fullname = tkinter.Label(membership_frame, text="Full Name : ")
lbl_fullname.grid(row=0,column=0, sticky="W")

entry_fullname = tkinter.Entry(membership_frame, width=50)
entry_fullname.grid(row=0,column=1, sticky="W")

lbl_address = tkinter.Label(membership_frame, text="Address : ")
lbl_address.grid(row=1,column=0,sticky="W")

entry_address = tkinter.Entry(membership_frame, width=50)
entry_address.grid(row=1,column=1,sticky="W")

lbl_birthdate = tkinter.Label(membership_frame, text="Birth Date : ")
lbl_birthdate.grid(row=2,column=0,sticky="W")

entry_birth = tkinter.Entry(membership_frame)
entry_birth.grid(row=2,column=1,sticky="W")

lbl_age = tkinter.Label(membership_frame, text="Age : ")
lbl_age.grid(row=3,column=0,sticky="W")

entry_age = tkinter.Entry(membership_frame)
entry_age.grid(row=3,column=1, sticky="W")

lbl_race = tkinter.Label(membership_frame, text="Race : ")
lbl_race.grid(row=4,column=0, sticky="W")

entry_race = ttk.Combobox(membership_frame, values=["Malay","Chinese","Indian","Bumiputera","Other"])
entry_race.grid(row=4,column=1, sticky="W")

lbl_religion = tkinter.Label(membership_frame, text="Religion : ")
lbl_religion.grid(row=5,column=0,sticky="w")

entry_religion = ttk.Combobox(membership_frame, values=["Islam","Christian","Buddha","Hindu","Other"])
entry_religion.grid(row=5,column=1, sticky="W")

lbl_email = tkinter.Label(membership_frame, text="E-mail : ")
lbl_email.grid(row=6,column=0,sticky="w")

entry_email = tkinter.Entry(membership_frame, width=20)
entry_email.grid(row=6,column=1,sticky="w")

lbl_phone = tkinter.Label(membership_frame, text="No.Phone : ")
lbl_phone.grid(row=7,column=0,sticky="w")

entry_phone = tkinter.Entry(membership_frame)
entry_phone.grid(row=7,column=1,sticky="w")

lbl_pay = tkinter.Label(membership_frame, text="----------PAYMENT--------")
lbl_pay.grid(row=8,column=0,sticky="W")

lbl_date_registration = tkinter.Label(membership_frame, text="Date Registration : ")
lbl_date_registration.grid(row=9,column=0, sticky="W")

entry_date = tkinter.Entry(membership_frame)
entry_date.grid(row=9,column=1, sticky="W")

lbl_fee = tkinter.Label(membership_frame, text="Membership fee (RM10) : ")
lbl_fee.grid(row=10,column=0)

lbl_payment = tkinter.Button(membership_frame, text="Please Pay Here!", command=pay)
lbl_payment.grid(row=10,column=1, sticky="W")

for widget in membership_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)    
    
# Account Frame
account_frame = tkinter.LabelFrame(frame, text="Create New Account as Membership")
account_frame.grid(row=1,column=1, padx=20,pady=20, sticky="NW") 

lbl_username = tkinter.Label(account_frame, text="Username : ")
lbl_username.grid(row=0,column=0,sticky="W")

entry_username = tkinter.Entry(account_frame)
entry_username.grid(row=0,column=1,sticky="W")

lbl_password = tkinter.Label(account_frame, text="Password : ")
lbl_password.grid(row=1,column=0)

entry_password = tkinter.Entry(account_frame)
entry_password.grid(row=1,column=1)   

for widget in account_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5) 
    
# ACCEPT TERMS FRAME
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)    
    
save_button = tkinter.Button(frame, text="SAVE & CREATE ACCOUNT", command=insert_data)
save_button.grid(row=3,column=0,ipadx=40, sticky="N")    

create_table()

window.mainloop()
