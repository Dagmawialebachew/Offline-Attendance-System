import csv  #used to read from and write to CSV files (like Excel tables)

# This functions reads student data from a CSV file
def read_students(filename):
    students = []  # We make an empty list to store student informations
    with open(filename, 'r') as file:  # Open the file in read mode
        reader = csv.reader(file)      # Use csv.reader to read the file line by line..
        next(reader)  # This skips the first row (the header part --> student_id, full_name)
