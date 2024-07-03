import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def save_tasks():
    tasks = listbox.get(0, listbox.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI layout
entry = tk.Entry(root, width=50)
entry.pack()

add_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=48, command=delete_task)
delete_button.pack()

save_button = tk.Button(root, text="Save Tasks", width=48, command=save_tasks)
save_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

# Start the main loop
root.mainloop()