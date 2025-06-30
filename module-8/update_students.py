# Paul Fralix, 06/29/2025, Assignment 8.2

import json

# Load JSON file into a Python class list
with open('student.json', 'r') as file:
    students = json.load(file)

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Output original list
print("This is the original Student list:")
print_students(students)

# Add your info to the class list
new_student = {
    "L_Name": "Fralix",
    "F_Name": "Paul",
    "Student_ID": "99999",
    "Email": "pfralix@aol.com"
}
students.append(new_student)

# Output updated list
print("\nThis is the updated Student list:")
print_students(students)

# Write back to JSON file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nNotification: The student.json file has been updated.")
