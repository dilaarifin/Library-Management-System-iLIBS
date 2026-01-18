from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox
import sqlite3

def home():
    window.destroy()
    import main

def login_success():
    messagebox.showinfo("Login Successful", "Welcome, Admin!")
    entry_username.delete(0, END)
    entry_password.delete(0, END)
    window.destroy()  # Close the login window
    import ict

def login():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    user = entry_username.get()
    code = entry_password.get()
    
    query = "SELECT * FROM ict WHERE name = ? AND id = ?"
    cursor.execute(query, (user, code))
    result = cursor.fetchone()
    
    if result is not None:
        # User credentials are valid
        login_success()
        
    else:
        # Invalid username or password
        messagebox.showerror("Login Failed", "Invalid username or password")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        prompt_try_again()
        
    conn.close()    
        
def prompt_try_again():
    result = messagebox.askretrycancel("Try Again", "Do you want to try again?")
    if result == True:
        entry_password.focus_set()  # Set focus back to username entry field
    else:
        window.destroy()  # Close the login window

# Create the main window
window = tk.Tk()
window.title("Welcome to iLIBS: Login ICT")
window.iconbitmap("icons/library.ico")
window.geometry("370x400")
window.resizable(False,False)
window.configure(relief='sunken', borderwidth=4)  

# Set the window size
window_width = 370
window_height = 400

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tkinter.Frame(window,bg="",relief='sunken',borderwidth=4)
frame.grid()

home_button = tk.Button(frame, text="HOME", command=home)
home_button.grid(row=0,column=0, sticky="W")

login_label = tkinter.Label(frame, text="LOGIN ICT", font=("Arial", 30, "bold"))
login_label.grid(row=1,column=0, padx=20,pady=10)

login_frame = tkinter.LabelFrame(frame)
login_frame.grid(row=2,column=0)

lbl_username = tkinter.Label(login_frame, text="Username : ")
lbl_username.grid(row=0,column=0)

entry_username = tkinter.Entry(login_frame, width=20)
entry_username.grid(row=0,column=1)

lbl_password = Label(login_frame, text="Password :")
lbl_password.grid(row=1,column=0,padx=5,pady=2)
password = StringVar()  # Create a StringVar for the password
entry_password = Entry(login_frame, show="*", textvariable=password)
entry_password.grid(row=1,column=1,padx=5,pady=2)

login_button = tkinter.Button(login_frame, text="LOG IN", command=login, bg="#76EE00", fg="black")
login_button.grid(row=3,column=1)

for widget in login_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)    

# Start the main event loop
window.mainloop()
