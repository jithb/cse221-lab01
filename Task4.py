# Lab 1 Task 4
# @author ChatGPT
# @license BRACU

from datetime import datetime

# Define a function to parse the departure time and create sorting criteria
def parse_train_info(line):
    parts = line.split(" at ")
    train_info, time_str = parts[0], parts[1]
    train_name = train_info.split(" will departure")[0]
    departure_time = datetime.strptime(time_str.strip(), "%H:%M")
    return train_name, departure_time, line

# Read input from 'input4.txt'
with open('input4.txt', 'r') as input_file:
    lines = input_file.readlines()

# First line is the number of schedules
N = int(lines[0].strip())

# Process each train schedule
trains = [parse_train_info(line.strip()) for line in lines[1:N + 1]]

# Sort trains by (1) train name lexicographically, (2) departure time in descending order, (3) input order
trains_sorted = sorted(trains, key=lambda x: (x[0], -x[1].hour * 60 - x[1].minute))

# Write the sorted output to 'output4.txt'
with open('output4.txt', 'w') as output_file:
    for _, _, original_line in trains_sorted:
        output_file.write(f"{original_line}\n")
