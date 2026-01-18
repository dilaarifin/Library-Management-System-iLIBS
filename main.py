import tkinter as tk

def loginict():
    window.destroy()
    import loginict

def loginuser():
    window.destroy()
    import userormembership       
    
def loginstaff():
    window.destroy()
    import loginstaff  # Import the desired module

# Main Window
window = tk.Tk()
window.title("Welcome to iLIBS: Library Management System (ILS)")
window.geometry("790x290")
window.iconbitmap("icons/library.ico")
window.resizable(False, False)
window.configure(padx=10, pady=10, bg="#F0F8FF", relief='sunken', borderwidth=4)

# Set the window size
window_width = 790
window_height = 290

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main Frame
frame = tk.Frame(window, bg="#F0F8FF")
frame.pack()

lbl_home = tk.Label(frame, text="HOME", font=("Arial", 30, "bold"), bg="#F0F8FF")
lbl_home.grid(row=0,column=0, sticky="W")

# User frame
user_frame = tk.LabelFrame(frame, text="iLIBS User", font=("Arial", 20, "bold"), bg="#8EE5EE")
user_frame.grid(row=1, column=0, padx=20, pady=10, ipadx=30, ipady=50, sticky="news")

user_button = tk.Button(user_frame, text="Click Here", font=("bold"), bg="#7AC5CD", command=loginuser)
user_button.grid(row=0, column=0, ipadx=15, ipady=10)

for widget in user_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Staff Frame
staff_frame = tk.LabelFrame(frame, text="iLIBS Staff", font=("Arial", 20, "bold"), bg="#FF6A6A")
staff_frame.grid(row=1, column=1, padx=20, pady=10, ipadx=30, ipady=50, sticky="news")

staff_button = tk.Button(staff_frame, text="Click Here", font=("bold"), bg="#EE6363", command=loginstaff)
staff_button.grid(row=0, column=0, ipadx=15, ipady=10)

for widget in staff_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)
    
ict_frame = tk.LabelFrame(frame, text="ICT Department", font=("Arial", 20, "bold"), bg="gray45")
ict_frame.grid(row=1,column=2, padx=20, pady=10, ipadx=30, ipady=50, sticky="news")    

ict_button = tk.Button(ict_frame, text="Click Here", font=("bold"), bg="gray47", command=loginict)
ict_button.grid(row=0, column=0, ipadx=15, ipady=10)

for widget in ict_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)
    
# Start the Tkinter event loop
window.mainloop()
