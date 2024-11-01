# Input for the numerators
num = input("Enter the numerators separated by spaces: ").split()
# Convert input strings to integers
num = [int(n) for n in num]

# Input for the denominators
denum = input("Enter the denominators separated by spaces: ").split()
# Convert input strings to integers
denum = [int(d) for d in denum]

# Check if the lengths of both lists are equal
if len(num) != len(denum):
    print("Error: The number of numerators must match the number of denominators.")
else:
    # Initialize lists to hold fractions
    fractions = []

    # Calculate the fractions
    for i in range(len(num)):
        fraction = num[i] / denum[i]
        fractions.append(fraction)

    # Find the smallest and largest fractions and their indices
    smallest_index = fractions.index(min(fractions))
    largest_index = fractions.index(max(fractions))
    
    smallest_fraction = fractions[smallest_index]
    largest_fraction = fractions[largest_index]

    # Print the results
    print(f"The smallest fraction is: {smallest_fraction} at index {smallest_index}")
    print(f"The largest fraction is: {largest_fraction} at index {largest_index}")
