# 1. File to list converter

filename =input("Enter a filename: ") # Ask for a filename

try: 
    with open(filename, "r") as file: # Read file
        lines = [line.strip() for line in file] # Read lines, strip whitespace and store in a list
    print(lines)
except FileNotFoundError: # Handle the case if file doesn't exist
    print(f"Error: The file '{filename}' was not found.")

# 2. Task list manager (with seperate module)

from tasks import add_task, remove_task # Import the module from the file tasks.py, importing the functions add_task and remove_task

my_tasks = [] # Start with an empty list

while True:
    action = input("Enter command: 'add <task>', 'remove <task>', or 'done': ").strip().lower() # Prompt the user for a command and transform it to lowercase

    if action == "done": # If the user enters 'done', exit the loop
        break

    if action.startswith("add "): # If the user enters a command starting with 'add ', extract the task and add it to the list
        task = action[4:].strip()
        add_task(my_tasks, task)
    elif action.startswith("remove "): # If the user enters a command starting with 'remove ', extract the task and remove it from the list
        task = action[7:].strip()
        remove_task(my_tasks, task)
    else: # If the user enters an invalid command, print an error message and continue the loop
        print("Invalid command. Use 'add <task>', 'remove <task>', or 'done'.")
        continue

    print(f"Updated task list: {my_tasks}") # Print the updated task list after each command