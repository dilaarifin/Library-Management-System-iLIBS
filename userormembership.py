import tkinter as tk

def home():
    window.destroy()
    import main
    
def user():
    window.destroy()
    import librarymember

def member():
    window.destroy()
    import loginmember  

# Main Window
window = tk.Tk()
window.title("Welcome to iLIBS: Library Management System (ILS)")
window.geometry("800x290")
window.iconbitmap("icons/library.ico")
window.resizable(False, False)
window.configure(padx=10, pady=10, bg="#F0F8FF", relief='sunken', borderwidth=4)

# Set the window size
window_width = 800
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

home_button = tk.Button(frame, text="HOME", command=home)
home_button.grid(row=0,column=0, sticky="W")

# User frame
user_frame = tk.LabelFrame(frame, text="Guest", font=("Arial", 30, "bold"), bg="#8EE5EE")
user_frame.grid(row=1, column=0, padx=20, pady=10, ipadx=30, ipady=50, sticky="news")

user_button = tk.Button(user_frame, text="Click Here", font=("bold"), bg="#7AC5CD", command=user)
user_button.grid(row=0, column=0, ipadx=15, ipady=10)

for widget in user_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Staff Frame
membership_frame = tk.LabelFrame(frame, text="User with Membership", font=("Arial", 30, "bold"), bg="#FF6A6A")
membership_frame.grid(row=1, column=1, padx=20, pady=10, ipadx=30, ipady=50, sticky="news")

membership_button = tk.Button(membership_frame, text="Click Here", font=("bold"), bg="#EE6363", command=member)
membership_button.grid(row=0, column=0, ipadx=15, ipady=10)

for widget in membership_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
