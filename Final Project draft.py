# program: Final Project GUI tkinter application
# author: Craig Blair
# created: updated draft 2025-04-28
# purpose: Help homeowners keep track of Maintenance tasks
# IDE: IDLE
# Used extra notes for personal reference 
# CodeAssist-AI: Used ChatPro to create this list of items.

# Pseudo:
# Define global variables for the main application window and list to store tasks.
# Define a function to initialize the main application window.
# Define a function to create and display the title and navigation buttons.
# Define a function to open a new window for scheduling tasks.
# Define a function to create input fields for task description, due date, and frequency selection.
# Define a function to create buttons for saving tasks, canceling, and returning to the main menu.
# Define a function to handle saving the task by collecting input and validating it.
# Define a function to open a new window to view scheduled tasks.
# Define a function to display the list of scheduled tasks in a listbox.
# Define a function to delete the selected task from the list.
# Define a function to mark the selected task as complete and remove it from the list.
# Define a function to open a help window explaining features and usage instructions.
# Call the main application to create an instance of the GUI and start the Tkinter event loop.

# Importing the required libraries
import tkinter as tk  # For creating the GUI window
from tkinter import messagebox, simpledialog  # For message dialogs
from tkinter import ttk  # For using themed widgets
from datetime import datetime  # For handling date objects

## Define the main class for the Home Maintenance Scheduler application
class HomeMaintenanceScheduler:
    def __init__(self, master):
        self.master = master  ## The main window
        master.title("OB Home Maintenance Scheduler")  

        # This will hold the list of tasks that the user adds
        self.tasks = []

        # Creating and packing GUI components
        # Title label
        self.title_label = tk.Label(master, text="OB Home Maintenance Scheduler", font=("Helvetica", 16))
        self.title_label.pack(pady=10)  ## Adding some vertical padding
        
        # Logo placeholder
        self.logo_label = tk.Label(master, text='[Logo/Image Here]', font=("Helvetica", 12))
        self.logo_label.pack(pady=5)

        # Navigation buttons for different functionalities
        self.schedule_task_button = tk.Button(master, text="Schedule New Task", command=self.open_schedule_task_window)
        self.schedule_task_button.pack(pady=5)  # Button to open the schedule task window

        self.view_tasks_button = tk.Button(master, text="View Scheduled Tasks", command=self.open_view_tasks_window)
        self.view_tasks_button.pack(pady=5)  # Button to view tasks

        self.help_button = tk.Button(master, text="Help", command=self.open_help_window)
        self.help_button.pack(pady=5)  # Button to open help window

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=5)  # Button to exit the application

        # Welcome message
        self.welcome_message = tk.Label(master, text="Manage your home maintenance tasks efficiently!", font=("Helvetica", 10))
        self.welcome_message.pack(pady=15)

    # Function to open the scheduling window
    def open_schedule_task_window(self):
        self.schedule_window = tk.Toplevel(self.master)  # Create a new window on top
        self.schedule_window.title("Schedule a New Maintenance Task")  # Title for the new window

        # Task description input
        tk.Label(self.schedule_window, text="Task Description:").pack(pady=5)
        self.task_description_entry = tk.Entry(self.schedule_window)
        self.task_description_entry.pack(pady=5)

        # Due date input
        tk.Label(self.schedule_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
        self.due_date_entry = tk.Entry(self.schedule_window)
        self.due_date_entry.pack(pady=5)

        # Frequency options (Daily, Weekly, Monthly)
        tk.Label(self.schedule_window, text="Frequency:").pack(pady=5)
        self.frequency_var = tk.StringVar(value="Monthly")  # Default value
        frequency_options = ["Daily", "Weekly", "Monthly", "Quarterly"]  # List of options
        self.frequency_menu = ttk.Combobox(self.schedule_window, textvariable=self.frequency_var, values=frequency_options)
        self.frequency_menu.pack(pady=5)

        # Save task button
        self.save_task_button = tk.Button(self.schedule_window, text="Save Task", command=self.save_task)
        self.save_task_button.pack(pady=5)

        # Cancel button
        self.cancel_button = tk.Button(self.schedule_window, text="Cancel", command=self.schedule_window.destroy)
        self.cancel_button.pack(pady=5)

    # Function to save the task from the entry fields
    def save_task(self):
        description = self.task_description_entry.get()  # Get task description
        due_date_str = self.due_date_entry.get()  # Get due date as string
        frequency = self.frequency_var.get()  # Get selected frequency

        if description and due_date_str:
            try:
                # Convert the due date from string to a date object
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                # Append the task data to the tasks list
                self.tasks.append({"description": description, "due_date": due_date, "frequency": frequency})
                messagebox.showinfo("Success", "Task saved successfully.")  # Show success message
                self.schedule_window.destroy()  # Close the scheduling window
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")  
        else:
            messagebox.showerror("Error", "Please fill in all fields.") 
    # Function to view scheduled tasks
    def open_view_tasks_window(self):
        # This creates a new window to display tasks
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Scheduled Maintenance Tasks")  # Title for the viewing window

        # Create a listbox to show tasks
        self.tasks_listbox = tk.Listbox(self.view_window, width=50)
        self.tasks_listbox.pack(pady=10)

        # Populate the listbox with scheduled tasks
        for index, task in enumerate(self.tasks):
            self.tasks_listbox.insert(index, f"{task['description']} - Due: {task['due_date'].strftime('%Y-%m-%d')} - Frequency: {task['frequency']}")  

        # Button to delete selected tasks
        self.delete_button = tk.Button(self.view_window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Button to mark tasks as complete
        self.complete_button = tk.Button(self.view_window, text="Mark as Complete", command=self.mark_task_complete)
        self.complete_button.pack(pady=5)

        # Button to go back to the main menu
        self.back_button = tk.Button(self.view_window, text="Back to Main Menu", command=self.view_window.destroy)
        self.back_button.pack(pady=5)

    # Function to delete a selected task from the list
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection() 
        if selected_task_index:  # Check if a task is selected
            del self.tasks[selected_task_index[0]]  # Delete from the tasks list
            self.tasks_listbox.delete(selected_task_index)  # Remove from the listbox
            messagebox.showinfo("Success", "Task deleted successfully.")  
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")  

    # Function to mark a task as complete
    def mark_task_complete(self):
        selected_task_index = self.tasks_listbox.curselection()  
        if selected_task_index:  # Check if a task is selected
            task_description = self.tasks[selected_task_index[0]]["description"]  
            messagebox.showinfo("Task Completed", f"Task '{task_description}' marked as complete.")  
            del self.tasks[selected_task_index[0]]  # Remove from tasks
            self.tasks_listbox.delete(selected_task_index)  # Remove from listbox
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    # Function to open the help window
    def open_help_window(self):
        self.help_window = tk.Toplevel(self.master)  # Create a help window
        self.help_window.title("Help and Support")  
        
        # Help text explaining the app features and instructions
        help_text = ("Welcome to OB Home Maintenance Scheduler!\n\n"
                     "Features:\n"
                     "- Schedule new maintenance tasks.\n"
                     "- View and manage scheduled tasks.\n"
                     "- Mark tasks as complete or delete them.\n\n"
                     "Instructions:\n"
                     "1. Click 'Schedule New Task' to add a maintenance task.\n"
                     "2. Enter the task details and click 'Save Task'.\n"
                     "3. Click 'View Scheduled Tasks' to see your tasks.\n"
                     "4. You can delete or mark tasks as complete from the list.\n\n"
                     "For support, please contact [obhomemaintence@gmail.com].")

        # Create a label in the help window to display the help text
        help_label = tk.Label(self.help_window, text=help_text, justify=tk.LEFT, padx=10, pady=10)
        help_label.pack()

        # Button to go back to the main menu
        self.back_button_help = tk.Button(self.help_window, text="Go Back to Main Menu", command=self.help_window.destroy)
        self.back_button_help.pack(pady=5)

# This block runs the application when the script is executed
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = HomeMaintenanceScheduler(root)  # Initialize the main application
    root.mainloop()  
