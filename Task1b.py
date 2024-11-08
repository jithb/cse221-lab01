# Lab 1 Task 1 B
# @author ChatGPT
# @license BRACU

# Open the input file and read all lines
with open('input1b.txt', 'r') as input_file:
    lines = input_file.readlines()

# First line is the number of test cases
T = int(lines[0].strip())

# List to store output lines
output_lines = []

# Process each test case
for i in range(1, T + 1):
    # Extract the expression after the "calculate" prefix
    expression = lines[i].strip().replace("calculate ", "")
    
    # Evaluate the expression safely
    try:
        result = eval(expression)
        output_lines.append(f"The result of {expression} is {result}")
    except Exception as e:
        # Handle any possible errors in expression evaluation
        output_lines.append(f"Error evaluating expression: {expression}")

# Write the results to the output file
with open('output1b.txt', 'w') as output_file:
    output_file.write("\n".join(output_lines))
