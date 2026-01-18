from tkinter import *
import tkinter 
import tkinter as tk
from tkinter import messagebox
import sqlite3

def home():
    window.destroy()
    import main

def back():
    window.destroy()
    import userormembership

def forgot():
    window.destroy()
    import forgotpassmember

def login_success():
    messagebox.showinfo("Login Successful", "Welcome, User!")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    window.destroy()
    import librarymember
    # Import 'loginuser' module if required, but consider importing at the beginning of the script

def login():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    user = entry_username.get()
    code = entry_password.get()
    
    # Query the database for the username and password
    query = "SELECT * FROM members WHERE member_user = ? AND member_pass = ?"
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

    # Close the database connection
    conn.close()
        
def prompt_try_again():
    result = messagebox.askretrycancel("Try Again", "Do you want to try again?")
    if result:
        entry_username.focus_set()  # Set focus back to username entry field
    else:
        window.destroy()  # Close the login window

def reg(): 
    window.destroy()
    import userwithmembership

# Create the main window
window = tk.Tk()
window.title("Welcome to iLIBS: Login As Member")
window.iconbitmap("icons/library.ico")
window.geometry("500x400")
window.resizable(False,False)
window.configure(relief='sunken', borderwidth=4)  

# Set the window size
window_width = 500
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
frame.pack()

home_button = tk.Button(frame, text="HOME", command=home)
home_button.grid(row=0,column=1, sticky="W")

back_button = tk.Button(frame, text="BACK", command=back)
back_button.grid(row=0,column=0, sticky="W")

login_label = tkinter.Label(frame, text="LOGIN as MEMBER", font=("Arial", 30, "bold"))
login_label.grid(row=1,column=0, padx=5,pady=5)

login_frame = tkinter.LabelFrame(frame)
login_frame.grid(row=2,column=0, sticky="news")

lbl_username = tkinter.Label(login_frame, text="Username: ")
lbl_username.grid(row=0,column=0)

entry_username = tkinter.Entry(login_frame, width=20)
entry_username.grid(row=0,column=1)

lbl_password = tkinter.Label(login_frame, text="Password: ")
lbl_password.grid(row=1,column=0)

entry_password = tkinter.Entry(login_frame, show="*", width=20)
entry_password.grid(row=1,column=1)

forgot_button = tk.Button(login_frame, text="Forgot Password?",bg="cyan3", command=forgot)
forgot_button.grid(row=2, column=1)

login_button = tkinter.Button(login_frame, text="LOG IN", bg="#76EE00", command=login)
login_button.grid(row=3,column=1)

lbl_or = tkinter.Label(login_frame, text="-------or-------")
lbl_or.grid(row=4,column=1)

signup_button = tkinter.Button(login_frame, text="SIGN UP", bg="tomato1", command=reg)
signup_button.grid(row=5,column=1)

for widget in login_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)    

# Start the main event loop
window.mainloop()
