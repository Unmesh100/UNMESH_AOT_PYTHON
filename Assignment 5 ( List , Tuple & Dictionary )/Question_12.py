# Taking input from the user
user_input = input("Enter numbers separated by spaces: ")

# Splitting the input string into a list of numbers (as strings)
numbers = user_input.split()

# Converting the list of strings to a list of floats (or integers)
number_list = [float(num) for num in numbers]

# Sorting the list
number_list.sort()

# Displaying the sorted list
print("Sorted list:", number_list)

# Finding the median
n = len(number_list)  # Get the number of elements

if n % 2 == 1:
    # If odd, the median is the middle element
    median = number_list[n // 2]
else:
    # If even, the median is the average of the two middle elements
    mid1 = number_list[n // 2 - 1]
    mid2 = number_list[n // 2]
    median = (mid1 + mid2) / 2

# Displaying the median
print("Median:", median)
