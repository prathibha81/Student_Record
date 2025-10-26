# File Handling
""" Student Record Management System"""
import os

print("--------------------STUDENT RECORD MANAGEMENT SYSTEM-------------------------")
Menu = print(" 1.Add Student Record\n 2.View Student Records\n 3.Exit")
def update_record_no():
    if os.path.exists("Student_records.txt"):
        with open("Student_records.txt","r") as f:
            lines = f.readlines()
            record_no = sum(1 for line in lines if line.strip().startswith("Record No:"))
            return record_no + 1
    else:
        return 1

def add_student_details():
    record_no = update_record_no()
    with open("Student_records.txt","a") as file:
         name = input("Enter Student Name: ")
         age = input("Enter Student Age: ")
         branch = input("Enter Student Branch: ")
         roll_no = input("Enter Student Roll No:")
         grades = input("Enter Student Grades: ")
         file.write("--------------------------------------------------\n")
         file.write(f"Record No: {record_no} ")
         file.write(f"\n Name: {name} \n Age: {age} \n Branch: {branch} \n Roll No: {roll_no} \n Grades: {grades}\n")
         file.write("--------------------------------------------------\n")
         print("Student record created successfully.")
         file.close()

def view_student_details():
    with open("Student_records.txt","r") as file:
        records = file.readlines()
        if records:
            for record in records:
                print(record.strip())
        else:
            print("No records found.")
        file.close()


    

while True:
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        add_student_details()
    elif choice == '2':
        view_student_details()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
