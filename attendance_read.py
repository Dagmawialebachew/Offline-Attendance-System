import csv  #used to read from and write to CSV files (like Excel tables)

# This function reads student data from a CSV file
def read_students(filename):
    students = []  # We make an empty list to store student information
    with open(filename, 'r') as file:  # Open the file in read mode
        reader = csv.reader(file)      # Use csv.reader to read the file line by line..
        next(reader)  # This skips the first row (the header part --> student_id, full_name)
        for row in reader:
            student_id = row[0]      # Get the student ID from the first column(accessing values by index from a list.)
            full_name = row[1]       # Get the full name from the second column -- list indexing.
            students.append([student_id, full_name])  # Add to the list of students
    return students  # Return the full list of students for further usage
