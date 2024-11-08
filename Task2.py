# Lab 1 Task 2
# @author ChatGPT
# @license BRACU

def bubbleSort(arr):
    # Bubble Sort with an optimization to achieve θ(n) for the best-case scenario
    for i in range(len(arr) - 1):
        swapped = False  # Initialize swapped as False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set swapped to True if a swap occurred
        # If no elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Explanation:
'''
The original Bubble Sort algorithm always runs in θ(n^2) time because it performs all passes
even if the array is already sorted. To improve this, we introduce a flag called `swapped`.
During each pass, if no elements are swapped, it means the array is already sorted, so we can
break out of the loop early. This modification reduces the time complexity to θ(n) in the
best-case scenario when the array is already sorted, as only one pass is needed to confirm 
the array's sorted state.
'''

# Read input from 'input2.txt'
with open('input2.txt', 'r') as input_file:
    lines = input_file.readlines()

# Extract array length and array elements from the input file
n = int(lines[0].strip())
arr = list(map(int, lines[1].strip().split()))

# Sort the array
bubbleSort(arr)

# Write the sorted array to 'output2.txt'
with open('output2.txt', 'w') as output_file:
    output_file.write(" ".join(map(str, arr)))
