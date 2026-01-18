import tkinter as tk
from tkinter import messagebox
import sqlite3

def pay():
    # Connect to the database
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Retrieve the account number and password from the entry fields
    account_number = entry_account.get()
    password = entry_pass.get()

    # Retrieve the current fund balance
    query = "SELECT fund FROM list_acc WHERE account_number = ? AND pass_acc = ?"
    cursor.execute(query, (account_number, password))
    current_fund = cursor.fetchone()

    if current_fund is not None:
        current_fund = current_fund[0]
        if current_fund >= 10:
            # Deduct RM10 from the user's fund
            new_fund = current_fund - 10

            # Update the fund balance in the database
            update_query = "UPDATE list_acc SET fund = ? WHERE account_number = ? AND pass_acc = ?"
            cursor.execute(update_query, (new_fund, account_number, password))
            conn.commit()

            messagebox.showinfo("Payment Successful", "Deducted RM10 from the user's fund.")
            entry_account.delete(0, tk.END)
            entry_pass.delete(0, tk.END)
            window.destroy()
        else:
            messagebox.showerror("Payment Failed", "Insufficient funds.")
    else:
        messagebox.showerror("Payment Failed", "Invalid account number or password.")

    # Close the database connection
    conn.close()

# Main Window
window = tk.Tk()
window.title("Welcome to iLIBS: Payment")
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

payment_frame = tk.LabelFrame(frame, text="Payment RM10")
payment_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

lbl_noacc = tk.Label(payment_frame, text="No Account: ")
lbl_noacc.grid(row=0, column=0, sticky="W")

entry_account = tk.Entry(payment_frame)
entry_account.grid(row=0, column=1, sticky="W")

lbl_pass = tk.Label(payment_frame, text="Password: ")
lbl_pass.grid(row=1, column=0, sticky="W")

entry_pass = tk.Entry(payment_frame, show="*")
entry_pass.grid(row=1, column=1, sticky="W")

pay_button = tk.Button(frame, text="PAY", bg="springgreen",command=pay)
pay_button.grid(row=2, column=0, ipadx=40, sticky="N")

for widget in payment_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

window.mainloop()
