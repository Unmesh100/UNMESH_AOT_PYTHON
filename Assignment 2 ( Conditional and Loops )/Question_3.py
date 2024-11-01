# Print the program introduction
print("Second Largest Number Finder")
print("-----------------------------")

# Get the number of elements to input
N = int(input("Enter the number of elements: "))

# Initialize variables to store the largest and second largest numbers
largest = float('-inf')
second_largest = float('-inf')

# Input the numbers and update the largest and second largest
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Print the second largest number
print(f"The second largest number is: {second_largest}")