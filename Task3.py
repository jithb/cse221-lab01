# Lab 1 Task 3
# @author ChatGPT
# @license BRACU

# Read input from 'input3.txt'
with open('input3.txt', 'r') as input_file:
    lines = input_file.readlines()

# First line is the number of students
N = int(lines[0].strip())

# Second line contains the student IDs
student_ids = list(map(int, lines[1].strip().split()))

# Third line contains the student marks
student_marks = list(map(int, lines[2].strip().split()))

# Combine student IDs and marks into a list of tuples
students = list(zip(student_ids, student_marks))

# Sort students by marks in descending order, and by ID in ascending order if marks are the same
students_sorted = sorted(students, key=lambda x: (-x[1], x[0]))

# Write the sorted output to 'output3.txt'
with open('output3.txt', 'w') as output_file:
    for student_id, mark in students_sorted:
        output_file.write(f"ID: {student_id} Mark: {mark}\n")
