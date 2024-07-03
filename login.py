import subprocess
import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

def open_Secondary(script_name):
    subprocess.run(["python", script_name])

def register():
    U_id = reg_U_id_entry.get()
    U_First_Name = reg_U_First_Name_entry.get()
    U_Middle_Name = reg_U_Middle_Name_entry.get()
    U_Last_Name = reg_U_Last_Name_entry.get()
    U_Email = reg_U_Email_entry.get()
    U_Ph_No = reg_U_ph_No_entry.get()
    U_password = reg_U_password_entry.get()

    con = mysql.connect(host="localhost", user="root", password="8520", database="USER")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM REGES WHERE U_id = %s", (U_id,))
    result = cursor.fetchone()

    if result:
        messagebox.showerror("Error", "ID already exists")
    else:
        cursor.execute("INSERT INTO REGES (U_id, U_First_Name, U_Middle_Name, U_Last_Name, U_Email, U_Ph_No, U_password) VALUES (%s,  %s, %s, %s, %s, %s, %s)",
                       (U_id, U_First_Name, U_Middle_Name, U_Last_Name, U_Email, U_Ph_No, U_password))
        con.commit()
        messagebox.showinfo("Status", "User Successfully Registered")

        # Clear the entry fields after registration
        reg_U_id_entry.delete(0, tk.END)
        reg_U_First_Name_entry.delete(0, tk.END)
        reg_U_Middle_Name_entry.delete(0, tk.END)
        reg_U_Last_Name_entry.delete(0, tk.END)
        reg_U_Email_entry.delete(0, tk.END)
        reg_U_ph_No_entry.delete(0, tk.END)
        reg_U_password_entry.delete(0, tk.END)

    con.close()

def login():
    U_id = login_U_id_entry.get()
    U_password = login_U_password_entry.get()
    con = mysql.connect(host="localhost", user="root", password="8520", database="USER")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM REGES WHERE U_id = %s AND U_password = %s", (U_id, U_password))
    result = cursor.fetchone()
   
    if result:
        messagebox.showinfo("Success", " Login successful")
        
    else:
        messagebox.showerror("Error", "Invalid  ID or password")

    # Clear the entry fields after Login
    login_U_id_entry.delete(0, tk.END)
    login_U_password_entry.delete(0, tk.END)

    con.close()

# Create main window
root = tk.Tk()
root.title("Login and Registration")
root.geometry("500x600")

# Registration frame
reg_frame = tk.Frame(root)
reg_frame.pack(pady=10)

tk.Label(reg_frame, text="Registration", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(reg_frame, text="User ID").grid(row=1, column=0, sticky='e', padx=10, pady=5)
reg_U_id_entry = tk.Entry(reg_frame)
reg_U_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="User First Name").grid(row=2, column=0, sticky='e', padx=10, pady=5)
reg_U_First_Name_entry = tk.Entry(reg_frame)
reg_U_First_Name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="User Middle Name").grid(row=3, column=0, sticky='e', padx=10, pady=5)
reg_U_Middle_Name_entry = tk.Entry(reg_frame)
reg_U_Middle_Name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="User Last Name").grid(row=4, column=0, sticky='e', padx=10, pady=5)
reg_U_Last_Name_entry = tk.Entry(reg_frame)
reg_U_Last_Name_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="User Email").grid(row=5, column=0, sticky='e', padx=10, pady=5)
reg_U_Email_entry = tk.Entry(reg_frame)
reg_U_Email_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="User Phone Number").grid(row=6, column=0, sticky='e', padx=10, pady=5)
reg_U_ph_No_entry = tk.Entry(reg_frame)
reg_U_ph_No_entry.grid(row=6, column=1, padx=10, pady=5)


tk.Label(reg_frame, text="Password").grid(row=7, column=0, sticky='e', padx=10, pady=5)
reg_U_password_entry = tk.Entry(reg_frame, show="*")
reg_U_password_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Button(reg_frame, text="Register", command=register).grid(row=8, column=0, columnspan=2, pady=10)

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_frame, text=" ID").grid(row=1, column=0, sticky='e', padx=10, pady=5)
login_U_id_entry = tk.Entry(login_frame)
login_U_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_frame, text="Password").grid(row=2, column=0, sticky='e', padx=10, pady=5)
login_U_password_entry = tk.Entry(login_frame, show="*")
login_U_password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_frame, text="Login",command=lambda:open_Secondary("home.py")).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()