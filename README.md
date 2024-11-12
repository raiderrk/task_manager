
# Task Manager CLI Application (Without Using Framework)


This CLI Task Manager is a simple command-line application designed to help users manage their to-do list. The application offers essential task management features such as adding, viewing, deleting, and marking tasks as completed. Tasks are saved to a file, allowing users to reload their task list on their next login, making it easy to keep track of tasks over time.

---

## Features

- **Login System**: Users must login with a  dummy username and password to access the task manager.
- **Add Task**: Create a new task by entering a task title.
- **View Tasks**: Display all tasks along with their completion status ("completed" or "not completed").
- **Delete Task**: Remove a task by entering its unique task ID.
- **Mark Task as Completed**: Update the status of a task to "completed" by providing the task ID.
- **Save & Exit**: Save all tasks to a file (`task.json`) before exiting. The next time the program is run, previously saved tasks will be reloaded automatically.

---

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python 3.x is installed on your computer. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. **Clone or Download the Project**: 
   - Clone this repository:
     ```bash
     git clone https://github.com/your-username/cli-task-manager.git
     ```
   - Or download the ZIP file and extract it.



---

## Running the Application

In the project directory, run the following command to start the application:

```bash
python task_manager.py

```
**Login Credentials (Testing Only):**

* Email: admin
* Password: password123


## Usage of this CLI Application

### Menu Options:

1. **Add a Task:** Create a new task by entering its title.
2. **View Tasks:** View a list of all tasks with their ID, title, and completion status.
3. **Delete a Task:** Delete a task by entering its specific ID.
4. **Mark a Task as Complete:** Update a task's status to "complete" using its ID.
5. **Exit:** Exit the application. All tasks will be saved automatically.

### Example Commands:

* **Adding a Task:** Choose option 1 and type the title for your new task.
* **Viewing Tasks:** Select option 2 to view all your tasks.
* **Deleting a Task:** Choose option 3, then enter the task ID to delete it.
* **Marking a Task as Complete:** Select option 4, then input the task ID to mark it as complete.
* **Exiting:** Choose option 5 to exit. Tasks will be saved automatically before exiting.

## File Structure

- `task_manager.py`: The main application file containing the logic for the task management system.
- `tasks.json`: A JSON file used to store task data, ensuring persistence between sessions.

## General Info

This application includes basic error handling for file operations and invalid task IDs to ensure smooth functionality.

