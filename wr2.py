# 1. File to list converter

filename =input("Enter a filename: ") # Ask for a filename

try: 
    with open(filename, "r") as file: # Read file
        lines = [line.strip() for line in file] # Read lines, strip whitespace and store in a list
    print(lines)
except FileNotFoundError: # Handle the case if file doesn't exist
    print(f"Error: The file '{filename}' was not found.")