
import csv
from datetime import datetime

def load_students(filename):
    students = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({'StudentID': row['StudentID'], 'FullName': row['FullName']})
        return students
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def take_attendance(students):
    attendance = []
    print("\nTaking Attendance (Enter 'P' for Present, 'A' for Absent):")
    for student in students:
        while True:
            status = input(f"{student['FullName']} ({student['StudentID']}): ").strip().upper()
            if status in ['P', 'A']:
                attendance.append({'StudentID': student['StudentID'], 'FullName': student['FullName'], 'Status': status})
                break
            else:
                print("Invalid input. Please enter 'P' or 'A'.")
    return attendance

def save_attendance(attendance, output_filename):
    with open(output_filename, mode='w', newline='') as file:
        fieldnames = ['StudentID', 'FullName', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(attendance)
    print(f"Attendance saved to '{output_filename}'.")

def main():
    input_file = 'students.csv'
    students = load_students(input_file)
    if students:
        attendance = take_attendance(students)
        date_str = datetime.now().strftime('%Y-%m-%d')
        output_file = f'attendance_{date_str}.csv'
        save_attendance(attendance, output_file)

if __name__ == '__main__':
    main()
