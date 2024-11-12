import json

class Task:

    def __init__(self,id,title,completed=False):
        self.id =id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id":self.id,"title": self.title , "Completed" :self.completed}   

tasks=[]

def addTask(title):    
        task_id = len(tasks)+1 
        task =Task(task_id, title)
        tasks.append(task)

        print("{}, Task added sucessfully".format(title))

def viewTask():    
        for task in tasks:
            if task.completed==True:
                status ="completed"
            else:
                status ="Not Completed"
            print("{}.{} = {}".format((task.id),(task.title),(status)))       


def deleteTask(task_id):    
        global tasks
        tasks = [task for task in tasks if task.id != task_id]
        print("{}, Task deleted Sucessfully.".format(task_id))  

def markTaskCompleted(task_id):    
        for task in tasks:
            if task.id ==task_id:
                task.completed =True 
                print("{}, Task marked as complete.".format(task_id))         
                break


def saveTask():
        with open("task.json","w") as file:
            json.dump([task.to_dict() for task in tasks],file)
        print("Task Saved Succesfully.") 
    
def loadTask():    
        global tasks

        try:

            with open('tasks.json',"r") as file:
                tasks_data = json.load(file)
                tasks.clear()
                for task_data in tasks_data:
                    task = Task(task_data["id"], task_data["title"], task_data["completed"])
                    tasks.append(task)
            print("Tasks loaded.")
        except FileNotFoundError:
            print("No saved tasks found.")


def main():    
        loadTask()  # Load tasks at the start
        while True:
            print("\nChoose 1Options: \n1. Add Task \n2. View Tasks \n3. Delete Task  \n4. Complete Task  \n5. Save & Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter task title: ")
                addTask(title)
            elif choice == "2":
                viewTask()
            elif choice == "3":
                task_id = int(input("Enter task ID to delete: "))
                deleteTask(task_id)
            elif choice == "4":
                task_id = int(input("Enter task ID to complete: "))
                markTaskCompleted(task_id)
            elif choice == "5":
                saveTask()
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
                      