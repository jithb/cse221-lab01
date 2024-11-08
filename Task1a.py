# Lab 1 Task 1 A
# @author ChatGPT
# @license BRACU

# Read input from the input file
with open('input1a.txt', 'r') as input_file:
    lines = input_file.readlines()

# First line is the number of test cases
T = int(lines[0].strip())

# List to store output lines
output_lines = []

# Process each test case
for i in range(1, T + 1):
    # Get the number N from the line
    N = int(lines[i].strip())
    
    # Determine if N is Odd or Even and add the result to output_lines
    if N % 2 == 0:
        output_lines.append(f"{N} is an Even number.")
    else:
        output_lines.append(f"{N} is an Odd number.")

# Write the results to the output file
with open('output1a.txt', 'w') as output_file:
    output_file.write("\n".join(output_lines))
