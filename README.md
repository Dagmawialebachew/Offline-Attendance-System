# Offline-Attendance-System
Project Description

-OAS is an attendance-taking system developed for instructors who use paper-based systems currently. 
-The system imports student names from a CSV file and makes teachers mark attendance through a simple command-line interface. 
-Key feature: Attendance is recorded as dated CSV files to be used afterwards.
-The solution decreases wastage of paperworks, makes it more precise, and simulates integration with a university database in a beginner-friendly approach.
  
Tools & Technologies Used

-Python
-Built-in `csv` module
-Git & GitHub

Features

-Load student list from a CSV file
-Mark attendance as Present (P) or Absent (A) for each student
-Save results in a new file named with today’s date (e.g., attendance_2025-05-20.csv)
-Works fully offline


How to setup and run the project

First, clone the repository 
   Open your terminal or Git Bash and run:
   git clone https://github.com/dagmawialebachew/offline-attendance-system.git
Navigate to the Project Directory

bash
Copy
Edit
cd smartattend-offline-attendance
Ensure Python 3 is installed
You can check with:

bash
Copy
Edit
python --version
Prepare your student list

Create a CSV file (e.g., students.csv) with two columns: StudentID and FullName.

Run the Attendance Script

bash
Copy
Edit
python smart_attend.py

Group Members

Dagmawi Tewodors   UGR/8286/17
Biruk Girma        UGR/6755/17
Tsinat Baheru      UGR/7832/17
Kalkidan Birhanu   UGR/1053/17
Fikir Yosef        UGR/3514/17
Hayat Adane        UGR/4156/17


