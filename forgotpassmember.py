import tkinter as tk
from tkinter import messagebox
import sqlite3

def update_password():
    # Retrieve the email and new password from the entry fields
    email = entry_account.get()
    new_password = entry_pass.get()

    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Update the password for the provided email
    update_query = "UPDATE members SET member_pass = ? WHERE member_email = ?"
    cursor.execute(update_query, (new_password, email))
    conn.commit()

    # Close the database connection
    conn.close()

    # Show appropriate message box based on the password update success
    if cursor.rowcount > 0:
        messagebox.showinfo("Password Updated", "Password updated successfully.")
        window.destroy()
        import loginmember
    else:
        messagebox.showinfo("Password Update Failed", "No matching email found.")
# Main Window
window = tk.Tk()
window.title("Welcome to iLIBS: Forgot Password (member)")
window.geometry("400x300")
window.iconbitmap("icons/library.ico")
window.resizable(False, False)

# Set the window size
window_width = 400
window_height = 300

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(window)
frame.pack()

forgot_frame = tk.LabelFrame(frame, text="Forgot Password")
forgot_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

lbl_noacc = tk.Label(forgot_frame, text="E-mail : ")
lbl_noacc.grid(row=0, column=0, sticky="W")

entry_account = tk.Entry(forgot_frame)
entry_account.grid(row=0, column=1, sticky="W")

lbl_pass = tk.Label(forgot_frame, text="New Password: ")
lbl_pass.grid(row=1, column=0, sticky="W")

entry_pass = tk.Entry(forgot_frame)
entry_pass.grid(row=1, column=1, sticky="W")

pay_button = tk.Button(frame, text="UPDATE PASSWORD", bg="cyan3", command=update_password)
pay_button.grid(row=2, column=0, ipadx=40, sticky="N")

for widget in forgot_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

window.mainloop()
