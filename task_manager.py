import json  # Import the json module to handle JSON data


# Dummy login function
# Dummy login function
def login():
    """Prompt the user for email and password, and check credentials."""
    email = input("Enter email: ")  # Get the user's email
    password = input("Enter password: ")  # Get the user's password

    # Check if the provided credentials match the expected values
    if email == "testuser@example.com" and password == "password123":
        print("Login successful!")  # Inform the user of a successful login
        return True  # Return True to indicate a successful login
    else:
        print("Invalid credentials. Please try again.")  # Inform the user of failure
        return False  # Return False to indicate a failed login


class Task:
    """Represents a task with an ID, title, and completion status."""

    def __init__(self, task_id, title):
        # Initialize the task with a unique identifier and a title
        self.id = task_id  # The unique ID for the task
        self.title = title  # The title or description of the task
        self.completed = False  # Initial status of the task (not completed)


tasks = []  # Initialize an empty list to store Task objects


def add_task(title):
    """Add a new task with a unique ID and given title."""
    task_id = len(tasks) + 1  # Assign a unique ID based on the current list length
    new_task = Task(task_id, title)  # Create a new Task object
    tasks.append(new_task)  # Add the new task to the tasks list


def view_tasks():
    """Display all tasks with their completion status."""
    for task in tasks:
        status = "vv" if task.completed else "XX"  # Check if the task is completed
        print(f"{task.id}: {task.title} [{status}]")  # Print task details


def delete_task(task_id):
    """Remove a task from the list by its ID."""
    global tasks  # Declare that we're modifying the global tasks list
    tasks = [task for task in tasks if task.id != task_id]  # Filter out the task with the given ID


def mark_task_complete(task_id):
    """Mark a task as completed based on its ID."""
    for task in tasks:
        if task.id == task_id:  # Find the task with the specified ID
            task.completed = True  # Set the task's completed status to True
            break  # Exit the loop after marking the task


def save_tasks(filename='tasks.json'):
    """Save the current list of tasks to a JSON file."""
    with open(filename, 'w') as file:  # Open the specified file in write mode
        json.dump([vars(task) for task in tasks], file)  # Serialize tasks to JSON format


def load_tasks(filename='tasks.json'):
    """Load tasks from a JSON file into the current task list."""
    global tasks  # Declare that we're using the global tasks list
    try:
        with open(filename, 'r') as file:  # Open the specified file in read mode
            tasks = [Task(**task) for task in json.load(file)]  # Deserialize JSON data into Task objects
    except FileNotFoundError:
        tasks = []  # If the file does not exist, initialize an empty task list


def main():
    """Main function to run the Task Manager CLI."""

    if not login():
        return  # Exit if login fails
    load_tasks()  # Load existing tasks from a file or storage
    while True:  # Start an infinite loop to keep the program running
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option: ")  # Get user choice

        if choice == '1':
            title = input("Enter task title: ")  # Prompt for task title
            add_task(title)  # Add the new task
        elif choice == '2':
            view_tasks()  # Display all tasks
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))  # Get ID of the task to delete
            delete_task(task_id)  # Delete the specified task
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))  # Get ID of the task to complete
            mark_task_complete(task_id)  # Mark the specified task as complete
        elif choice == '5':
            save_tasks()  # Save tasks before exiting
            print("Exiting...")  # Inform the user of the exit
            break  # Exit the loop and the program
        else:
            print("Invalid choice, please try again.")  # Handle invalid input


if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly
