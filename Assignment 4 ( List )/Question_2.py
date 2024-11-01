# Input for the first list
L = input("Enter the elements of the first list separated by spaces: ").split()
# Convert the input strings to integers
L = [int(x) for x in L]

# Input for the second list
M = input("Enter the elements of the second list separated by spaces: ").split()
# Convert the input strings to integers
M = [int(x) for x in M]

# Check if both lists are of the same size
if len(L) != len(M):
    print("The lists must be of the same size.")
else:
    # Initialize an empty list for the results
    N = []

    # Add corresponding elements of L and M
    for i in range(len(L)):
        N.append(L[i] + M[i])

    # Print the resulting list
    print("The resulting list N is:", N)
