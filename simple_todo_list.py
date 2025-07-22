import tkinter as tk
from tkinter import messagebox
todo_list = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_list:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        todo_list.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        todo_list.remove(task)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="skyblue")

heading = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="skyblue")
heading.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="skyblue")
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, width=12)
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task, width=12)
remove_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(btn_frame, text="Exit", command=exit_app, width=12)
exit_btn.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=45, height=10, font=("Helvetica", 12))
listbox.pack(pady=20)

root.mainloop()
