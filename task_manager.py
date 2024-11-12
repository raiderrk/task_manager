import json  # Importing the JSON module to handle JSON data

# Dummy credentials for user authentication
USER_CREDENTIALS = {
    "username": "admin",
    "password": "password123"
}

# Function to prompt user for login credentials and verify them
def login():
    print("Please login here:")
    username = input("Username: ")
    password = input("Password: ")
    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Please try again.\n")
        return False


# Class representing a Task with id, title, and completion status
class Task:

    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    # Method to convert the Task object to a dictionary format (for JSON storage)
    def to_dict(self):
        return {"id": self.id, "title": self.title, "Completed": self.completed}

# List to store all Task instances
tasks = []

# Function to add a new task to the list
def addTask(title):
    task_id = len(tasks) + 1  # Generate a unique task ID
    task = Task(task_id, title)  # Create a new Task object
    tasks.append(task)  # Add the new task to the list
    print("{}, Task added successfully".format(title))

# Function to display all tasks with their completion status
def viewTask():
    for task in tasks:
        status = "completed" if task.completed else "Not Completed"  # Set task status based on completion
        print("{}.{} = {}".format(task.id, task.title, status))

# Function to delete a task by its ID
def deleteTask(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]  # Filter out the task with the specified ID
    print("{}, Task deleted successfully.".format(task_id))

# Function to mark a task as completed based on its ID
def markTaskCompleted(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True  # Set task completion status to True
            print("{}, Task marked as complete.".format(task_id))
            break

# Function to save all tasks to a JSON file
def saveTask():
    try:
        with open("task.json", "w") as file:
            json.dump([task.to_dict() for task in tasks], file)  # Convert tasks to dictionary format and save to file
        print("Task saved successfully.")
    except Exception as e:
        print(f'Error saving tasks: {e}')  # Handle file writing errors

# Function to load tasks from a JSON file at startup
def loadTask():
    global tasks

    try:
        with open('tasks.json', "r") as file:
            tasks_data = json.load(file)  # Load JSON data from file
            tasks.clear()  # Clear any existing tasks
            for task_data in tasks_data:
                task = Task(task_data["id"], task_data["title"], task_data["completed"])  # Recreate Task objects
                tasks.append(task)  # Add each task to the list
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

# Main function to run the program
def main():
    if not login():  # Call login function and check credentials
        return  # Exit if login fails
    
    loadTask()  # Load tasks at the start
    while True:
        # Display menu options for the user
        print("\nChoose an Option: \n1. Add Task \n2. View Tasks \n3. Delete Task \n4. Complete Task \n5. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            addTask(title)  # Add a new task
        elif choice == "2":
            viewTask()  # View all tasks
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            deleteTask(task_id)  # Delete a specified task
        elif choice == "4":
            task_id = int(input("Enter task ID to complete: "))
            markTaskCompleted(task_id)  # Mark a specified task as completed
        elif choice == "5":
            saveTask()  # Save tasks and exit
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
