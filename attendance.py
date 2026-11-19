print("STUDENT ATTENDANCE SYSTEM")

students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students[student_id] = name
    print("Student added successfully!")

def mark_attendance():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        status = input("Enter Present or Absent: ")
        students[student_id] = students[student_id] + " - " + status
        print("Attendance updated successfully!")
    else:
        print("Student not found!")

def display_students():
    print("\nStudent Attendance Details:")
    for student_id, details in students.items():
        print(student_id, ":", details)

add_student()
mark_attendance()
display_students()
print("Attendance feature updated successfully!")
