import tkinter as tk
from tkinter import messagebox

def add_task():
    task=entry.get()
    if task!="":
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messeagebox.showwarning("Warning","task can't be empty")

def remove_task():
    try:
        selected=listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to remove!")

def update_task():
    try:
        selected=listbox.curselection()[0]
        new_task=entry.get
        if new_task!="":
            listbox.delete(selected)
            listbox.insert(selected,new_task)
            entry.delete(0,tk.END)
        else:
            masseagebox.showwarning("Warning","Please select a task to update!")
    except IndexError:
        messagebox.showarning("Warning","Please select a task to update!")


def exit_app():
    root.destroy()

#GUI setup

root=tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#f5f5f5")

# Input field
entry=tk.Entry(root,width=30,font=("Arial",14))
entry.pack(pady=10)

#BUTTONS

btn_framework=tk.Frame(root,bg="#f5f5f5")
btn_framework.pack(pady=5)



tk.Button(btn_framework,text="Add Task", width=10,command=add_task).grid(row=0,column=0,padx=5)

tk.Button(btn_framework,text="Remove Task",width=10,command=remove_task).grid(row=0,column=1,padx=5)


tk.Button(btn_framework,text="Update Task", width=10,command=update_task).grid(row=0,column=2,padx=5)

tk.Button(root,text="Exit",width=10,command=exit_app).pack(pady=5)


#Task list
listbox=tk.Listbox(root,width=40,font=("Arial",12))
listbox.pack(pady=10)


root.mainloop()
