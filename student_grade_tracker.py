import csv
from prettytable import PrettyTable

# Path to your CSV file
file_path = "student_grades.csv"

# Data structure to store student data
students = {}

# Function to load student data from the CSV file

def load_data():
    try:
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) < 4:
                    continue  # Skip any incomplete rows
                roll_number, name, subject, grade = row
                roll_number = roll_number.strip()  # Remove any extra spaces from roll_number
                grade = float(grade)  # Convert grade to float
                
                # Check if the roll number already exists
                if roll_number not in students:
                    students[roll_number] = {"name": name, "grades": {}}
                students[roll_number]["grades"][subject] = grade
        
        print("Data loaded successfully from the file.")
        print(f"Loaded Students: {students}")  # Debugging statement to show loaded data
        
    except FileNotFoundError:
        print(f"No file found at {file_path}. Starting with empty data.")

# Function to add a new student
def add_student():
    name = input("Enter Student Name: ").strip()
    roll_number = input("Enter Roll Number: ").strip()
    if roll_number in students:
        print("Student with this roll number already exists!")
        return
    students[roll_number] = {"name": name, "grades": {}}
    print("Student added successfully!")

# Function to add grades for a student
def add_grades():
    roll_number = input("Enter Roll Number: ").strip()
    if roll_number not in students:
        print("Student not found!")
        return
    print("Enter grades for the following subjects:")
    subjects = input("Enter subjects separated by commas (e.g., Math,Science,English): ").split(",")
    for subject in subjects:
        subject = subject.strip()
        while True:
            try:
                grade = float(input(f"Enter grade for {subject}: "))
                if 0 <= grade <= 100:
                    students[roll_number]["grades"][subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
    print("Grades added successfully!")

# Function to view the report of a specific student
def view_report():
    roll_number = input("Enter Roll Number: ").strip()
    if roll_number not in students:
        print("Student not found!")
        return
    student = students[roll_number]
    print(f"\nStudent: {student['name']} (Roll No: {roll_number})")
    print("-" * 40)
    table = PrettyTable(["Subject", "Grade"])
    for subject, grade in student["grades"].items():
        table.add_row([subject, grade])
    print(table)
    if student["grades"]:
        avg = sum(student["grades"].values()) / len(student["grades"])
        print(f"Total Average: {avg:.2f}\n")
    else:
        print("No grades available for this student.")

# Function to view all students
def view_all_students():
    if not students:
        print("No students available!")
        return
    print("\nAll Students:")
    print("-" * 40)
    table = PrettyTable(["Roll Number", "Name", "Total Average"])
    for roll_number, data in students.items():
        if data["grades"]:
            avg = sum(data["grades"].values()) / len(data["grades"])
        else:
            avg = 0.0
        table.add_row([roll_number, data["name"], f"{avg:.2f}"])
    print(table)

# Function to export data to the specified CSV file
def export_data():
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Subject", "Grade"])  # Header row
        for roll_number, data in students.items():
            for subject, grade in data["grades"].items():
                writer.writerow([roll_number, data["name"], subject, grade])
    print(f"Data exported to {file_path} successfully!")

# Main function to handle the program workflow
def main():
    load_data()  # Load data at the start of the program
    while True:
        print("\nSTUDENT GRADE TRACKER")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. View Report")
        print("4. View All Students")
        print("5. Export Data")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            view_report()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            export_data()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
