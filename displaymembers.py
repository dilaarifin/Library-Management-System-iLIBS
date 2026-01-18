from tkinter import *
import tkinter 
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def display_data():
    
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
    member_password = entry_password.get()
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, member_name, member_address, member_birth, member_age, member_race, member_religion, member_email, member_phone,member_date, member_user, member_pass FROM members")
    rows = cursor.fetchall()
    conn.close()

    listmember_display.delete(0, tk.END)
    for row in rows:
        id_member, member_name, member_address, member_birth, member_age, member_race, member_religion, member_email, member_phone, member_date, member_user, member_password = row
        listmember_display.insert(tk.END, f"ID: {id_member}")
        listmember_display.insert(tk.END, f"Name: {member_name}")
        listmember_display.insert(tk.END, f"Address: {member_address}")
        listmember_display.insert(tk.END, f"Birth: {member_birth}")
        listmember_display.insert(tk.END, f"Age: {member_age}")
        listmember_display.insert(tk.END, f"Race: {member_race}")
        listmember_display.insert(tk.END, f"Religion: {member_religion}")
        listmember_display.insert(tk.END, f"Email: {member_email}")
        listmember_display.insert(tk.END, f"Phone: {member_phone}")
        listmember_display.insert(tk.END, f"Date Registration: {member_date}")
        listmember_display.insert(tk.END, f"Username: {member_user}")
        listmember_display.insert(tk.END, f"Password: {member_password}")
        listmember_display.insert(tk.END, "-" * 40)
        

def update_data():
    selected_item = listmember_display.curselection()
    
    if not selected_item:
        return
    
    new_fullname = entry_fullname.get()
    new_address = entry_address.get()
    new_birthdate = entry_birth.get()
    new_age = entry_age.get()
    new_race = entry_race.get()
    new_religion = entry_religion.get()
    new_email = entry_email.get()
    new_phone = entry_phone.get()
    new_date = entry_date.get()
    new_username = entry_username.get()
    new_password = entry_password.get()
    
    selected_item_text = listmember_display.get(selected_item[0])
    selected_item_id = selected_item_text.split(':')[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET member_name=?, member_address=?, member_birth=?, member_age=?, member_race=?, member_religion=?, member_email=?, member_phone=?, member_date=?, member_user=?, member_pass=? WHERE id=?", (new_fullname, new_address, new_birthdate, new_age, new_race, new_religion, new_email, new_phone, new_date, new_username, new_password, selected_item_id))
    conn.commit()
    conn.close()

    entry_fullname.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_birth.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_race.delete(0, tk.END)
    entry_religion.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    
    display_data()

def delete_data():
    selected_item = listmember_display.curselection()
    if not selected_item:
        return

    selected_id = listmember_display.get(selected_item).split(":")[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id=?", (selected_id,))
    conn.commit()
    conn.close()

    display_data()

# Create the main window
window = tk.Tk()
window.title("Welcome to iLIBS: Display Members")
window.iconbitmap("icons/library.ico")
window.geometry("1000x600")
window.resizable(False,False)
window.configure(relief='sunken', borderwidth=4)  

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

frame = tkinter.Frame(window,bg="",relief='sunken',borderwidth=4)
frame.pack()

lbl = tkinter.Label(frame, text="List Of Members", font=("arial", 30, "bold"))
lbl.grid(row=0,column=0)

first_frame = tkinter.LabelFrame(frame, text="List Members")
first_frame.grid(row=1,column=0)

second_frame = tkinter.LabelFrame(frame, text="Update Here")
second_frame.grid(row=1,column=1,padx=10)

listmember_display = tkinter.Listbox(first_frame, width=65, height=27)
listmember_display.grid(row=0,column=0, padx=10, pady=10, sticky="news")

toolsframe = tkinter.LabelFrame(frame, text="Tools")
toolsframe.grid(row=2,column=0,padx=10)

display_button = tkinter.Button(toolsframe, text="Display Members", command=display_data, bg="#800080", fg="white")
display_button.grid(row=0,column=0)

update_button = tkinter.Button(toolsframe, text="Update Member", command=update_data, bg="#1E90FF", fg="black")
update_button.grid(row=0,column=1)

delete_button = tkinter.Button(toolsframe, text="Delete", command=delete_data, bg="#FF3030", fg="white")
delete_button.grid(row=0,column=2)

for widget in toolsframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)    

# second frame
lbl_fullname = tkinter.Label(second_frame, text="Full Name : ")
lbl_fullname.grid(row=0,column=0, sticky="W")

entry_fullname = tkinter.Entry(second_frame, width=50)
entry_fullname.grid(row=0,column=1, sticky="W")

lbl_address = tkinter.Label(second_frame, text="Address : ")
lbl_address.grid(row=1,column=0,sticky="W")

entry_address = tkinter.Entry(second_frame, width=50)
entry_address.grid(row=1,column=1,sticky="W")

lbl_birthdate = tkinter.Label(second_frame, text="Birth Date : ")
lbl_birthdate.grid(row=2,column=0,sticky="W")

entry_birth = tkinter.Entry(second_frame)
entry_birth.grid(row=2,column=1,sticky="W")

lbl_age = tkinter.Label(second_frame, text="Age : ")
lbl_age.grid(row=3,column=0,sticky="W")

entry_age = tkinter.Entry(second_frame)
entry_age.grid(row=3,column=1, sticky="W")

lbl_race = tkinter.Label(second_frame, text="Race : ")
lbl_race.grid(row=4,column=0, sticky="W")

entry_race = ttk.Combobox(second_frame, values=["Malay","Chinese","Indian","Bumiputera","Other"])
entry_race.grid(row=4,column=1, sticky="W")

lbl_religion = tkinter.Label(second_frame, text="Religion : ")
lbl_religion.grid(row=5,column=0,sticky="w")

entry_religion = ttk.Combobox(second_frame, values=["Islam","Christian","Buddha","Hindu","Other"])
entry_religion.grid(row=5,column=1, sticky="W")

lbl_email = tkinter.Label(second_frame, text="E-mail : ")
lbl_email.grid(row=6,column=0,sticky="w")

entry_email = tkinter.Entry(second_frame, width=20)
entry_email.grid(row=6,column=1,sticky="w")

lbl_phone = tkinter.Label(second_frame, text="No.Phone : ")
lbl_phone.grid(row=7,column=0,sticky="w")

entry_phone = tkinter.Entry(second_frame)
entry_phone.grid(row=7,column=1,sticky="w")

lbl_date_registration = tkinter.Label(second_frame, text="Date Registration : ")
lbl_date_registration.grid(row=9,column=0, sticky="W")

entry_date = tkinter.Entry(second_frame)
entry_date.grid(row=9,column=1, sticky="W")

lbl_username = tkinter.Label(second_frame, text="Username : ")
lbl_username.grid(row=10,column=0,sticky="W")

entry_username = tkinter.Entry(second_frame)
entry_username.grid(row=10,column=1,sticky="W")

lbl_password = tkinter.Label(second_frame, text="Password : ")
lbl_password.grid(row=11,column=0,sticky="W")

entry_password = tkinter.Entry(second_frame)
entry_password.grid(row=11,column=1,sticky="W")  

for widget in second_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)    
    
# Start the main event loop
window.mainloop()
