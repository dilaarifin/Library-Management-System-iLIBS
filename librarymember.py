from tkinter import * 
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, publisher TEXT, department TEXT, isbn TEXT, noshelf TEXT, status INTEGER,  member_name TEXT, member_id INTEGER)")
    conn.commit()
    conn.close()

def display_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, publisher, department, isbn, noshelf, status, member_name, member_id FROM books")
    rows = cursor.fetchall()
    conn.close()

    listbook_display.delete(0, tk.END)
    for row in rows:
        id_book, title_book, author_book, publisher_book, department_book, isbn_book, noshelf_book, status_book, member_name, member_id = row
        display_text = f"ID: {id_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Title: {title_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Author: {author_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Publisher: {publisher_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Department: {department_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"ISBN: {isbn_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"No Shelf: {noshelf_book}"
        listbook_display.insert(tk.END, display_text)
        
        if status_book == 1:
            status_text = "Status: Available"
        else:
            status_text = f"Status: Not Available (Lent to {member_name} - ID: {member_id})"
        
        listbook_display.insert(tk.END, status_text)
        listbook_display.insert(tk.END, "-" * 40)

def search_data():
    search_query = entry_search.get()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, publisher, department, isbn, noshelf, status FROM books WHERE title LIKE ? OR author LIKE ? OR publisher LIKE ? OR department LIKE ? OR isbn LIKE ? OR noshelf LIKE ?",
                   (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
    rows = cursor.fetchall()
    conn.close()

    listbook_display.delete(0, tk.END)
    for row in rows:
        id_book, title_book, author_book, publisher_book, department_book, isbn_book, noshelf_book, status_book = row
        display_text = f"ID: {id_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Title: {title_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Author: {author_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Publisher: {publisher_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"Department: {department_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"ISBN: {isbn_book}"
        listbook_display.insert(tk.END, display_text)
        display_text = f"No Shelf: {noshelf_book}"
        listbook_display.insert(tk.END, display_text)
        status_text = "Status: Available" if status_book == 1 else "Status: Not Available"
        listbook_display.insert(tk.END, status_text)
        listbook_display.insert(tk.END, "")

def list_book():
    selected_value = rb1_var.get()
    if selected_value == 1:  # All Books
        display_data()
    elif selected_value == 2:  # In Library (Available Books)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, publisher, department, isbn, noshelf, status FROM books WHERE status = 1")
        rows = cursor.fetchall()
        conn.close()
        listbook_display.delete(0, tk.END)
        if rows:
            for row in rows:
                id_book, title_book, author_book, publisher_book, department_book, isbn_book, noshelf_book, status_book = row
                display_text = f"ID: {id_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Title: {title_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Author: {author_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Publisher: {publisher_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Department: {department_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"ISBN: {isbn_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"No Shelf: {noshelf_book}"
                listbook_display.insert(tk.END, display_text)
                status_text = "Status: Available"
                listbook_display.insert(tk.END, status_text)
                listbook_display.insert(tk.END, "")
        else:
            listbook_display.insert(tk.END, "No available books.")
    elif selected_value == 3:  # Borrowed Books (Not Available Books)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, publisher, department, isbn, noshelf, status FROM books WHERE status = 0")
        rows = cursor.fetchall()
        conn.close()
        listbook_display.delete(0, tk.END)
        if rows:
            for row in rows:
                id_book, title_book, author_book, publisher_book, department_book, isbn_book, noshelf_book, status_book = row
                display_text = f"ID: {id_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Title: {title_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Author: {author_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Publisher: {publisher_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"Department: {department_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"ISBN: {isbn_book}"
                listbook_display.insert(tk.END, display_text)
                display_text = f"No Shelf: {noshelf_book}"
                listbook_display.insert(tk.END, display_text)
                status_text = "Status: Not Available"
                listbook_display.insert(tk.END, status_text)
                listbook_display.insert(tk.END, "")
        else:
            listbook_display.insert(tk.END, "No borrowed books.")
    
# Main Window        
window = tk.Tk()
window.title("Welcome to iLIBS: Library Management System (ILS)")
window.geometry("1070x700")
window.iconbitmap("icons/library.ico")

# Set the window size
window_width = 1070
window_height =700

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(window, bg="")
frame.pack()

# frames
top_frame = tkinter.LabelFrame(frame, text="Tool Bars")
top_frame.grid(row=0,column=0,sticky="news")

lbl_userlibrary = tkinter.Label(frame, text="Welcome to Library (Only View)", font=("Arial", 30, "bold"))
lbl_userlibrary.grid(row=0,column=0)

display_frame = tkinter.LabelFrame(frame, text="List Books")
display_frame.grid(row=1,column=0, padx=10, pady=10, sticky="news")

# frame search
search_frame = tkinter.LabelFrame(frame, text="Search")
search_frame.grid(row=1,column=1,padx=10, pady=10, sticky="news")

lbl_search = tkinter.Label(search_frame, text="Search : ")
lbl_search.grid(row=0,column=0,padx=10, pady=1,)

entry_search = tkinter.Entry(search_frame, width=45)
entry_search.grid(row=0,column=1)

search_button = tkinter.Button(search_frame, text="SEARCH",command=search_data, bg="#76EE00", fg="black")
search_button.grid(row=0,column=2)

for widget in search_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

crudframe = tkinter.LabelFrame(frame)
crudframe.grid(row=3,column=0)

display_button = tkinter.Button(crudframe, text="DISPLAY",command=display_data, bg="#4287f5", fg="black")
display_button.grid(row=0,column=0,ipadx=10,ipady=7,padx=5,pady=5)

# Create list_bar LabelFrame
list_bar = tkinter.LabelFrame(frame)
list_bar.grid(row=3, column=1, padx=5, pady=5)

# Create Radiobuttons
rb1_var = tkinter.IntVar()
rb1 = tkinter.Radiobutton(list_bar, text="All Books", value=1, variable=rb1_var)
rb2 = tkinter.Radiobutton(list_bar, text="In Library", value=2, variable=rb1_var)
rb3 = tkinter.Radiobutton(list_bar, text="Borrowed Books", value=3, variable=rb1_var)

rb1.grid(row=0, column=0, padx=5, pady=5)
rb2.grid(row=0, column=1, padx=5, pady=5)
rb3.grid(row=0, column=2, padx=5, pady=5)

# Create List Books button
list_button = tkinter.Button(list_bar, text="LIST BOOKS", command=list_book, bg="#EEC900", fg="black")
list_button.grid(row=0, column=3, padx=5, pady=5)

# Configure padding for all widgets inside list_bar
for widget in list_bar.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# displays
listbook_display = tkinter.Listbox(display_frame, width=70, height=27)
listbook_display.grid(row=0,column=0, padx=10, pady=10, sticky="news")

create_table()

window.mainloop()