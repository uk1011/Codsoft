import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkbootstrap import Style

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("360x490")
        self.title("To Do List")
        self.iconbitmap("todolist.ico")

        self.style = Style(theme='minty')
        self.create_widgets()

    def create_widgets(self):

        # label of to do list app
        title_label = ttk.Label(self, text="To Do List", font=("Helvetica 20 bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # entry to input task
        self.task_entry = ttk.Entry(self, width=30)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # button to add task
        self.addtask_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.addtask_button.grid(row=1, column=1, padx=5, pady=10)

        # listbox to store and display tasks
        self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # scrollbar for listbox
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.task_listbox.yview)
        scrollbar.grid(row=2, column=2, sticky="ns")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # edit task button
        self.edittask_button = ttk.Button(self, text="Edit Task", command=self.edit_task)
        self.edittask_button.grid(row=3, column=0, padx=5)

        # delete task button
        self.deletetask_button = ttk.Button(self, text="Delete Task", command=self.delete_task)
        self.deletetask_button.grid(row=3, column=1, padx=5)

        # frame to organize buttons
        button_frame = ttk.Frame(self)
        button_frame.grid(row=4, column=0, columnspan=2, pady=5)

        # save task button
        self.savetask_button = ttk.Button(button_frame, text="Save Tasks", command=self.save_task)
        self.savetask_button.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # load task button
        self.loadtask_button = ttk.Button(button_frame, text="Load Tasks", command=self.load_task)
        self.loadtask_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # function to add tasks
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    # function to edit tasks
    def edit_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            selected_task = self.task_listbox.get(task_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, selected_task)
            self.task_listbox.delete(task_index)

    # function to delete tasks
    def delete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            self.task_listbox.delete(task_index)

    # function to save tasks to file in txt file format
    def save_task(self):
        tasks = self.task_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for task in tasks:
                    file.write(task + '\n')

    # function to load tasks from file from txt file
    def load_task(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                tasks = file.readlines()
                self.task_listbox.delete(0, tk.END)
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())


if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()
