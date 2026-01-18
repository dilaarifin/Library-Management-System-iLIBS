import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def reg_staff():
    import staffregistration
    
def list_staff():
    import liststaff    

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # Librarian info
        name = name_entry.get()
        responsibility = responsibility_combobox.get()

        if name and responsibility:
            availability = availability_combobox.get()
            age = age_combobox.get()
            id = id_combobox.get()

            # Librarian ICT info
            registration_status = reg_status_var.get()
            contactnum = contactnum_combobox.get()
            numexperience = numexperience_combobox.get()

            print("Name: ", name, "Responsibility: ", responsibility)
            print("Availability: ", availability, "Age: ", age, "ID: ", id)
            print("# Contact Number: ", contactnum, "# Years of Experience: ", numexperience)
            print("Registration status", registration_status)
            print("------------------------------------------")

            # Create Table
            conn = sqlite3.connect('database.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS ict
                    (name TEXT, responsibility TEXT, availability TEXT, age INT, id TEXT, 
                    registration_status TEXT, contact_num INT, num_experience INT)
            '''
            conn.execute(table_create_query)

            # Insert Data
            data_insert_query = '''INSERT INTO ict (name, responsibility, availability, 
            age, id, registration_status, contact_num , num_experience) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (name, responsibility, availability,
                                 age, id, registration_status, contactnum, numexperience)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully added to database",icon='info')

        else:
            tkinter.messagebox.showwarning(title="Error", message="Name and responsibility are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

def display_data():
    # Function to display the data from the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ict")
    rows = cursor.fetchall()
    conn.close()

    display_box.delete(0, tkinter.END)
    for row in rows:
        name, responsibility, availability, age, id, registration_status, contact_num, num_experience = row
        display_box.insert(tkinter.END, f"ID: {id}")
        display_box.insert(tkinter.END, f"Name: {name}")
        display_box.insert(tkinter.END, f"Responsibility: {responsibility}")
        display_box.insert(tkinter.END, f"Availability: {availability}")
        display_box.insert(tkinter.END, f"Age: {age}")
        display_box.insert(tkinter.END, f"Registration Status: {registration_status}")
        display_box.insert(tkinter.END, f"Contact Number: {contact_num}")
        display_box.insert(tkinter.END, f"Years of Experience: {num_experience}")
        display_box.insert(tkinter.END, "-" * 40)

def update_data():
    selected_item = display_box.curselection()
    
    if not selected_item:
        return
    
    # Function to update the data in the database
    new_id = id_combobox.get()
    new_responsibility = responsibility_combobox.get()
    new_name = name_entry.get()
    new_availability = availability_combobox.get()
    new_age = age_combobox.get()
    new_contactnum = contactnum_combobox.get()
    new_numexperience = numexperience_combobox.get()

    selected_item_text = display_box.get(selected_item[0])
    selected_item_id = selected_item_text.split(':')[1].strip()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE ict SET name=?, responsibility=?, availability=?, age=?, contact_num=?, num_experience=? WHERE id=?", (new_id, new_name, new_responsibility, new_availability, new_age, new_contactnum, new_numexperience, selected_item_id))
    conn.commit()
    print("Data updated successfully.")

    display_data()  # Update the data displayed in the interface
    conn.close()

def delete_data():
    selected_item = display_box.curselection()
    if not selected_item:
        return

    selected_text = display_box.get(selected_item[0])
    selected_id = selected_text.split(":")[1].strip()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ict WHERE id = ?", (selected_id,))
    conn.commit()
    conn.close()
    print("Data deleted successfully.")

    display_data()


window = tkinter.Tk()
window.title("ICT Department")

accept_var = tkinter.StringVar(value="Not Accepted") 

frame = tkinter.Frame(window)
frame.grid(row=0, column=0, sticky="w", padx=20, pady=10)

# ICT Librarian Details
librarian_frame = tkinter.LabelFrame(frame, text="ICT Librarian Info")
librarian_frame.grid(row= 0, column=0, sticky="w", padx=20, pady=10)

name_label = tkinter.Label(librarian_frame, text="Name")
name_entry = tkinter.Entry(librarian_frame)
name_label.grid(row=0, column=0)
name_entry.grid(row=1, column=0)

availability_label = tkinter.Label(librarian_frame, text="Availability")
availability_combobox = ttk.Combobox(librarian_frame, values=["", "Yes", "No"])
availability_label.grid(row=0, column=1)
availability_combobox.grid(row=1, column=1)

age_label = tkinter.Label(librarian_frame, text="Age")
age_combobox = ttk.Combobox(librarian_frame, values=[str(i) for i in range(25, 41)])
age_label.grid(row=0, column=2)
age_combobox.grid(row=1, column=2)

id_label = tkinter.Label(librarian_frame, text="ID")
id_combobox = ttk.Combobox(librarian_frame, values=["95517", "95519", "95520", "95521", "95528", "96610", "96615",
                                                     "96627", "96630", "96634"])
id_label.grid(row=2, column=0)
id_combobox.grid(row=3, column=0)

responsibility_label = tkinter.Label(librarian_frame, text="Responsibility")
responsibility_combobox = ttk.Combobox(librarian_frame, values=["Cataloging", "Acquisition", "Librarian ICT", "Corporate Unit",
                                                                "Documentation Unit", "Circulation", "Financial Unit",
                                                                "Chief Librarian", "Assistant Librarian"])
responsibility_label.grid(row=2, column=1)
responsibility_combobox.grid(row=3, column=1)

for widget in librarian_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

librarian_frame = tkinter.LabelFrame(frame, text="Librarian Info")
librarian_frame.grid(row=1, column=0, sticky="w", padx=20, pady=10)

registered_label = tkinter.Label(librarian_frame, text="ICT Librarian Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(librarian_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

contactnum_label = tkinter.Label(librarian_frame, text="# Contact Number")
contactnum_combobox = ttk.Entry(librarian_frame)
contactnum_label.grid(row=0, column=1)
contactnum_combobox.grid(row=1, column=1)

numexperience_label = tkinter.Label(librarian_frame, text="# Years of Experience")
numexperience_combobox = ttk.Combobox(librarian_frame, values=["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                                                               "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                               "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
                                                               "36", "37", "38", "39", "40"])
numexperience_label.grid(row=0, column=2)
numexperience_combobox.grid(row=1, column=2)

for widget in librarian_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Buttons
button_frame = tkinter.Frame(window)
button_frame.grid(row=3, column=0, sticky="w", padx=20, pady=10)

tool_bar = tkinter.LabelFrame(frame, text="Tools for ICT Display")
tool_bar.grid(row=3, column=0, sticky="W")

enter_button = tkinter.Button(tool_bar, text="Enter Data", command=enter_data, bg="#76EE00", fg="black")
enter_button.grid(row=0, column=0, padx=5)

display_button = tkinter.Button(tool_bar, text="Display Data", command=display_data, bg="#800080", fg="white")
display_button.grid(row=0, column=1, padx=5)

update_button = tkinter.Button(tool_bar, text="Update Data", command=update_data, bg="#1E90FF", fg="black")
update_button.grid(row=0, column=2, padx=5)

delete_button = tkinter.Button(tool_bar, text="Delete Data", command=delete_data, bg="#FF3030", fg="white")
delete_button.grid(row=0, column=3, padx=5)

for widget in tool_bar.winfo_children():
    widget.grid_configure(padx=5, pady=5)

staff_frame = tkinter.LabelFrame(frame, text="For Staffs")
staff_frame.grid(row=3,column=0, sticky="E")

registerstaff_button = tkinter.Button(staff_frame, text="Register Staff", bg="deeppink1", command=reg_staff)
registerstaff_button.grid(row=0, column=0, padx=5)

liststaff_button = tkinter.Button(staff_frame, text="List Staff", bg="deeppink2", command=list_staff)
liststaff_button.grid(row=0,column=1, padx=5)

for widget in staff_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="w", padx=20, pady=10)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Display Data Box
display_frame = tkinter.LabelFrame(window, text="Data Display")
display_frame.grid(row=0, column=1, rowspan=3, sticky="news", padx=20, pady=10)

scrollbar = tkinter.Scrollbar(display_frame)
scrollbar.pack(side="right", fill="y")

display_box = tkinter.Listbox(display_frame, yscrollcommand=scrollbar.set, width=100)
display_box.pack(side="left", fill="both")

scrollbar.config(command=display_box.yview)

window.mainloop()
