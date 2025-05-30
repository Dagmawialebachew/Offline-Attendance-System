from datetime import datetime
from attendance_intro_ui import welcome_message, teacher_name
from attendance_reader import read_students
from attendance_saver import save_attendance
from attendance_marker import mark_attendance


# This is the main function that controls the whole program to proceed step by step....
def main():

  choice = welcome_message() #Get the the welcome_msg function from the imported attedance-intro-ui.py
  if choice != '1':
        print("The program is exited")
        exit()

  teacher_name = teacher_name() #Get also the teacher_name from the imported teacher_name function.
  print(f"\nHello {teacher_name}, let's take attendance\n") #Ask the Lecuter's name to create better user experience, and save files according to specific Lecuters
  
  # Get today's date as a string (e.g. "2025-05-29")
  today = datetime.now().strftime("%Y-%m-%d")
  
  print(f"Taking attendance for: {today}")  # Show today's date
  
  # Load students from CSV file using the function imported from attendace-reader py file
  students = read_students("students.csv")
  
  # Mark their attendance file using the function imported from attedance-marker.py file
  attendance = mark_attendance(students)
  
  #Save the attendance to a CSV file using the function declared in attendace-saver.py
  save_attendance(attendance, today, teacher_name)

# Run the main function to start the program
main()
