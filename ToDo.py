import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(task_index, updated_task)
        entry_task.delete(0, tk.END)
    except IndexError:
        pass

def load_selected_task(event):
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, selected_task)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry
entry_task = tk.Entry(root, width=40)
entry_task.grid(row=0, column=0, padx=5, pady=5)

# Task list
listbox_tasks = tk.Listbox(root, height=10, width=40)
listbox_tasks.grid(row=1, column=0, padx=5, pady=5)

# Buttons
button_add_task = tk.Button(root, text="Add Task", width=12, command=add_task)
button_add_task.grid(row=0, column=1, padx=5, pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=12, command=delete_task)
button_delete_task.grid(row=1, column=1, padx=5, pady=5)

button_update_task = tk.Button(root, text="Update Task", width=12, command=update_task)
button_update_task.grid(row=2, column=1, padx=5, pady=5)

# Load selected task on click
listbox_tasks.bind('<<ListboxSelect>>', load_selected_task)

root.mainloop()
