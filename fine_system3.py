import tkinter as tk
from tkinter import ttk
import sqlite3

def create_table():
    conn = sqlite3.connect("fine_system.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS fine (username TEXT, fineperday INTEGER, totaldaysdue INTEGER, totalbook INTEGER, bookname TEXT, paymentamount INTEGER)")
    conn.commit()
    conn.close()

def insert_data():
    username = username_entry.get()
    fineperday = fineperday_entry.get()
    totaldaysdue = totaldaysdue_entry.get()
    totalbook = totalbook_spinbox.get() 
    bookname = bookname_entry.get()
    paymentamount = fine_amount_entry.get() 
    
    conn = sqlite3.connect("fine_system.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fine (username, fineperday, totaldaysdue, totalbook, bookname, paymentamount) VALUES (?, ?, ?, ?, ?,?)", (username, fineperday, totaldaysdue, totalbook, bookname,paymentamount))
    conn.commit()
    conn.close()

    username_entry.delete(0, tk.END)
    fineperday_entry.delete(0, tk.END)
    totaldaysdue_entry.delete(0, tk.END)
    totalbook_spinbox.delete(0, tk.END)
    bookname_entry.delete(0, tk.END)
    fine_amount_entry.delete(0, tk.END)
    
def fine_amount():
    fineperday = 0.20
    totaldaysdue = int(totaldaysdue_entry.get())
    totalbook = int(totalbook_spinbox.get())
    fine = fineperday * totaldaysdue * totalbook

    label_output.config(text=f'Total Fine Amount = RM{fine :.2f}')

window = tk.Tk()
window.title("Fine Log")
window.configure(bg="light pink")

frame = tk.Frame(window)
frame.grid()

username_label = tk.Label(window, text="Username:", bg="light pink")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(window, width = 40, justify = "center")
username_entry.grid(row=1, column=0)

fine_label = tk.Label(window, text="Fine per day is RM0.20", bg="light pink")
fine_label.grid(row=2, column=0)

calculate_label = tk.Label(window, text="fine amount = fine per day X total days due X total book", bg="light pink")
calculate_label.grid(row=3, column=0)

fineperday_label = tk.Label(window, text="Fine per day:", bg="light pink")
fineperday_label.grid(row=4, column=0)
fineperday_entry = tk.Entry(window, width = 40, justify = "center")
fineperday_entry.grid(row=5, column=0)

totaldaysdue_label = tk.Label(window, text="Total days due:", bg="light pink")
totaldaysdue_label.grid(row=6, column=0)
totaldaysdue_entry = tk.Entry(window, width = 40, justify = "center")
totaldaysdue_entry.grid(row=7, column=0)

totalbook_label = tk.Label(window, text="Total number of Books:", bg="light pink")
totalbook_label.grid(row=8, column=0)
totalbook_spinbox = ttk.Spinbox(window, from_ = 0, to = 20, width = 38, justify = "center")
totalbook_spinbox.grid(row=9, column=0)

bookname_label = tk.Label(window, text="Book Name:", bg="light pink")
bookname_label.grid(row=10, column=0)
bookname_entry = tk.Entry(window, width = 40, justify = "center")
bookname_entry.grid(row=11, column=0)

payment_button = tk.Button(window, text="Calculate Fine", command=fine_amount, width = 35, bg = "royal blue", fg = "white")
payment_button.grid(row=12, column=0, padx=20, pady=10)

label_output = tk.Label(window, bg="light pink")
label_output.grid(row=13, column=0, padx=20, pady=10)

fine_label = tk.Label(window, text="Enter fine amount here:", bg="light pink")
fine_label.grid(row=14,column=0)

fine_amount_entry = tk.Entry(window)
fine_amount_entry.grid(row = 15, column = 0)

enterdata_button = tk.Button(window, text="Enter Data", command=insert_data, width = 35, bg = "royal blue", fg = "white")
enterdata_button.grid(row=17,column=0, padx=20, pady=10)

for widget in window.winfo_children():  #winfo stands for widget info
    widget.grid_configure(padx = 20, pady = 7)

create_table()
window.mainloop()
