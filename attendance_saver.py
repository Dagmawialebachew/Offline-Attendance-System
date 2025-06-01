import csv
# This function saves the attendance records into a new CSV file
def save_attendance(attendance, today,t_name):
    # File name e.g. attendance_2025-05-29.csv
    filename = t_name + "_attendance_" + today + ".csv"
    
    with open(filename, 'w', newline='') as file:  # Open file in write mode
        writer = csv.writer(file)  # Use csv.writer to write to file
        
        # Write the header row (column names)
        writer.writerow(['student_id', 'full_name', 'status'])
        
        # Write each attendance record to the file
        for record in attendance:
            writer.writerow(record)
    
    # Print confirmation message after saving
    print(f"\n✅ Attendance saved in {filename}")
