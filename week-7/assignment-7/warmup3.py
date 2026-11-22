import os

current_directory = os.getcwd()
print("Current directory:", current_directory)
file_exists = os.path.exists("week-7/data/notes.txt")
print("Does notes.txt exist?", file_exists)
file_path = os.path.join("week-7", "data", "notes.txt")
print("File path:", file_path)