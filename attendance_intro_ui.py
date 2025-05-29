def welcome_message(): #define a function to welcome users(Lecturer)
    
    print(" Welcome to OAS--Offline Attendance System: ")
    print("1. Take Attendance")
    print("2. Exit")
    ch = input('Choose an option: ')
    return ch

def teacher_name(): #define another function to get the teacher's name.
     t_name = input("\nEnter your name: ")
     
     if t_name == '':
      print('Teacher name must be filled.')
      exit()
      
     return t_name # Return the teacher's name, making it usable in different files.
