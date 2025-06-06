def mark_attendance(students): #define a function that mark the attendance for the students.
  attendance_list = []  # Empty list to store each student's attendance record
  print("\nEnter P for Present, A or any key for Absent\n")  # Instructions to the user
  for student in students:
          student_id = student[0]
          full_name = student[1]
          
          # Ask for input (P or A)
          status = input(f"{student_id} - {full_name}: ").upper()  # Convert input to uppercase
          
          # If the teacher enters anything other than P, mark as A (Absent) by default:
          if status != 'P':
              status = 'A'
  
          
          # Add the attendance record to the list (convert 'P' to 'Present', 'A' to 'Absent')
          attendance_list.append([student_id, full_name, 'Present' if status == 'P' else 'Absent'])
      
  return attendance_list  # Return the full attendance list
