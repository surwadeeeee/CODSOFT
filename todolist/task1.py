import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning please enter a task.")

def delete_task():
    try:
       selected_index = listbox.curselection()
       if selected_index:
           listbox.delete(selected_index)
       else:
        messagebox.showwarning("warning please select a task to delete.")
    except:
       pass

def update_task():
    try:
        selected_index = listbox.curselection()
        updated_task = entry.get()
        if selected_index and updated_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to update.")
    except:
        pass
window = tk.Tk()
window.title("To-Do List")

listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)


scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=20)


add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=2)
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=2)
update_button = tk.Button(window, text="Update Task", command=update_task)
update_button.pack(pady=2)
window.mainloop()
