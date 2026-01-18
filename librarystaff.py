from tkinter import * 
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def pay():
    import fine_system3

def members():
    import displaymembers

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, publisher TEXT, department TEXT, isbn TEXT, noshelf TEXT, status INTEGER, member_name TEXT, member_id INTEGER)")
    conn.commit()
    conn.close()

def lend_book():
    selected_item = listbook_display.curselection()
    if not selected_item:
        return
    
    selected_id = listbook_display.get(selected_item[0]).split(':')[1].strip()
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM books WHERE id=?", (selected_id,))
    status = cursor.fetchone()
    
    if status and status[0] == 1:
        # Get member information
        member_name = entry_member_name.get()
        member_id = entry_member_id.get()
        
        if member_name and member_id:
            # Update book status and insert member information
            cursor.execute("UPDATE books SET status=?, member_name=?, member_id=? WHERE id=?", (0, member_name, member_id, selected_id))
            conn.commit()
            messagebox.showinfo("Success", "Book successfully lent to member", icon='info')
            display_data()
        else:
            messagebox.showwarning("Error", "Please enter member information")
    else:
        messagebox.showwarning("Error", "Book is not available")
    
    conn.close()


def retrieve_book():
    selected_item = listbook_display.curselection()
    if not selected_item:
        return

    selected_id = listbook_display.get(selected_item[0]).split(':')[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM books WHERE id=?", (selected_id,))
    status = cursor.fetchone()

    if status and status[0] == 0:
        cursor.execute("UPDATE books SET status=? WHERE id=?", (1, selected_id))  # Update status to 1 (book available)
        conn.commit()
        messagebox.showinfo("Success", "Book successfully retrieved", icon='info')
    else:
        messagebox.showwarning("Error", "Book is already available")

    conn.close()
    display_data()


def insert_data():
    title_book = entry_titlebook.get()
    author_book = entry_author.get()
    publisher_book = entry_publisher.get()
    department_book = entry_department.get()
    isbn_book = entry_isbn.get()
    noshelf_book = entry_noshelf.get()
    status_book = 1  # Assuming a default status of 1 (book in the library)
    
    if title_book and author_book and publisher_book and department_book and isbn_book and noshelf_book:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, publisher, department, isbn, noshelf, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (title_book, author_book, publisher_book, department_book, isbn_book, noshelf_book, status_book))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Successfully added to database", icon='info')

        entry_titlebook.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_publisher.delete(0, tk.END)
        entry_department.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)
        entry_noshelf.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Error", message="Fields cannot be empty", icon="warning")

    
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

    
def update_data():
    selected_item = listbook_display.curselection()
    
    if not selected_item:
        return

    new_title = entry_titlebook.get()
    new_author = entry_author.get()
    new_publisher = entry_publisher.get()
    new_department = entry_department.get()
    new_isbn = entry_isbn.get()
    new_noshelf = entry_noshelf.get()

    selected_item_text = listbook_display.get(selected_item[0])
    selected_item_id = selected_item_text.split(':')[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, publisher=?, department=?, isbn=?, noshelf=? WHERE id=?", (new_title, new_author, new_publisher, new_department, new_isbn, new_noshelf, selected_item_id))
    conn.commit()
    conn.close()

    entry_titlebook.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_publisher.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
    entry_noshelf.delete(0, tk.END)

    display_data() 

def delete_data():
    selected_item = listbook_display.curselection()
    if not selected_item:
        return

    selected_id = listbook_display.get(selected_item).split(":")[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (selected_id,))
    conn.commit()
    conn.close()

    display_data()

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
window.title("Welcome to iLIBS: Library Management System (ILS)             [Librarian Department]")
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

frame = tk.Frame(window)
frame.pack()

# frames
top_frame = tkinter.LabelFrame(frame, text="Tool Bars")
top_frame.grid(row=0,column=0,sticky="news")

right_frame = tkinter.LabelFrame(frame, text="Members")
right_frame.grid(row=0,column=1,sticky="news")

display_other = tkinter.LabelFrame(frame, text="Add Book / Update / Display / Delete (Books)")
display_other.grid(row=1, column=1, sticky="news")

display_frame = tkinter.LabelFrame(frame, text="List Books")
display_frame.grid(row=1,column=0, padx=10, pady=10, sticky="news")

# frame search
search_frame = tkinter.LabelFrame(frame, text="Search")
search_frame.grid(row=3,column=0,padx=10, pady=10, sticky="news")

lbl_search = tkinter.Label(search_frame, text="Search : ")
lbl_search.grid(row=0,column=0,padx=10, pady=1,)

entry_search = tkinter.Entry(search_frame, width=45)
entry_search.grid(row=0,column=1)

search_button = tkinter.Button(search_frame, text="SEARCH",command=search_data, bg="#FFB6C1", fg="black")
search_button.grid(row=0,column=2)

for widget in search_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# CRUD frame

addbook_button = tkinter.Button(display_other, text="ADD BOOK", command=insert_data, bg="#76EE00", fg="black")
addbook_button.grid(row=10,column=0,pady=40, padx=5, sticky="E")

update_button = tkinter.Button(display_other, text="UPDATE",command=update_data, bg="#1E90FF", fg="black")
update_button.grid(row=10,column=1, pady=40, padx=5)

display_button = tkinter.Button(display_other, text="DISPLAY",command=display_data, bg="#4287f5", fg="black")
display_button.grid(row=10,column=2,pady=40, padx=5)

delete_button = tkinter.Button(display_other, text="DELETE",command=delete_data, bg="#FF3030", fg="black")
delete_button.grid(row=10,column=3,pady=40, padx=5)

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
listbook_display = tkinter.Listbox(display_frame, width=65, height=27)
listbook_display.grid(row=0,column=0, padx=10, pady=10, sticky="news")

# display other

lbl_titlebook = tkinter.Label(display_other, text="Title Book : ")
lbl_titlebook.grid(row=0,column=0)

entry_titlebook = tkinter.Entry(display_other)
entry_titlebook.grid(row=0,column=1)

lbl_author = tkinter.Label(display_other, text="Author : ")
lbl_author.grid(row=1,column=0)

entry_author = tkinter.Entry(display_other)
entry_author.grid(row=1,column=1)

lbl_publisher = tkinter.Label(display_other, text="Publisher : ")
lbl_publisher.grid(row=2,column=0)

entry_publisher = tkinter.Entry(display_other)
entry_publisher.grid(row=2,column=1)

lbl_department = tkinter.Label(display_other, text="Department : ")
lbl_department.grid(row=3,column=0)

entry_department = tkinter.Entry(display_other)
entry_department.grid(row=3,column=1)

lbl_isbn = tkinter.Label(display_other, text="ISBN : ")
lbl_isbn.grid(row=4, column=0)

entry_isbn = tkinter.Entry(display_other)
entry_isbn.grid(row=4,column=1)

lbl_noshelf = tkinter.Label(display_other, text="No Shelf : ")
lbl_noshelf.grid(row=5,column=0)

entry_noshelf = tkinter.Entry(display_other)
entry_noshelf.grid(row=5,column=1)

for widget in display_other.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# tool bars
lendbook_button = tkinter.Button(top_frame, text="Lend Book", command=lend_book, bg="#8B5A00", fg="white")
lendbook_button.grid(row=0,column=1,ipadx=10,ipady=7,padx=5,pady=5)

lbl_who = tkinter.Label(top_frame, text="Who Lend the Book?", font=("arial", 10, "bold"))
lbl_who.grid(row=0,column=2, columnspan=2, padx=5,pady=5)

lbl_member_name = tkinter.Label(top_frame, text="Enter Name : ")
lbl_member_name.grid(row=1,column=2, padx=5,pady=5, sticky="N")

entry_member_name = tkinter.Entry(top_frame)
entry_member_name.grid(row=1,column=3, padx=5,pady=5, sticky="N")

lbl_member_id = tkinter.Label(top_frame, text="ID : ")
lbl_member_id.grid(row=2,column=2, sticky="E", padx=5,pady=5)

entry_member_id = tkinter.Entry(top_frame)
entry_member_id.grid(row=2,column=3, padx=5,pady=5)

retrieve_button = tkinter.Button(top_frame, text="Retrieve Book",command=retrieve_book, bg="#FFA500", fg="black")
retrieve_button.grid(row=0,column=6,ipadx=10,ipady=7,padx=5,pady=5)

pay_button = tkinter.Button(top_frame, text="Fine Log",command=pay, bg="#FF3030", fg="white")
pay_button.grid(row=0,column=7,ipadx=10,ipady=7,padx=5,pady=5)

listmembers_button = tkinter.Button(right_frame, text="List Members",command=members, bg="#800080", fg="white")
listmembers_button.grid(row=0,column=0,ipadx=10,ipady=7,padx=5,pady=5,sticky="E")


create_table()

window.mainloop()