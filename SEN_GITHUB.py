# Student Course Registration System

students = {}
courses = ["CSC201", "MTH202", "GST203", "PHY204"]
registrations = {}

def register_student():
    username = input("Enter username: ")
    password = input("Enter password: ")
    students[username] = password
    print("Registration successful!\n")

def login_student():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in students and students[username] == password:
        print("Login successful!\n")
        register_course(username)
    else:
        print("Invalid login details\n")

def display_courses():
    print("Available Courses:")
    for course in courses:
        print(course)

def register_course(username):
    display_courses()
    selected = input("Enter course code to register: ")
    if selected in courses:
        registrations[username] = selected
        print("Course registered successfully!\n")
    else:
        print("Invalid course selection\n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        login_student()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")