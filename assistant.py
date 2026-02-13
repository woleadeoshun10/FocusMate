import datetime  # This import will handle dates

#PerosnalAssistant Class
class PersonalAssistant:
    def __init__(self):
        self.tasks = [] #Created an empty list to store tasks as dictionaries
        

    #Method to add a new task
    def add_task(self,description,due_time=None):
        task = {
            "description": description,   #Text to add to task
            "due_time": due_time,         #Optional Due date
            "done": False                #Task is default to Not complete
        }
        self.tasks.append(task)         #Add the task dictionary to the tasks list
        print(f"✅ Task added : {description}")  # Print Confirmation
        
        
    #Method to display all tasks
    def show_tasks(self):
        if not self.tasks:              #Check if task list is empty
            print(f"🎉 No tasks! You are all clear.")       #Print message if no tasks
            return                      #Exit 
        print("\n📌 Your Tasks:")       #Print the Header for tasks
        for i, task in enumerate(self.tasks, start=1):   #Loop through the tasks starting from 1
            status = "✔️" if task["done"] else "❌"  #Show check if done, cross if not
            due = f"(due {task['due_time']})" if task["due_time"] else""  #Show due date if it exits
            print(f"{i}. {task['description']} {status} {due}")  #Print the task number, description , status and its due time.
    
    #Method to mark a task as completed
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):     #Check if index is valid
            self.tasks[index]["done"] = True  #Mark task as done
            print(f"🎯 Completed: {self.tasks[index]['description']}")  #Print confirmation
        else:
            print("⚠️ Invalid task number.")  #Print error if index is invalid
                

#Test
assistant = PersonalAssistant()  #Create a new PersonalAssistant Object
assistant.show_tasks()  #No task added 

assistant.add_task("Finish Coding Challenge", datetime.date(2025,8,20))  #Add task with due date
assistant.add_task("Call my Mom")  #Add task with no due date

assistant.show_tasks()   #Display all tasks
assistant.complete_task(0)  #Mark first task as done
assistant.show_tasks()      #Display updated tasks to show completion
            
        
    
    



