# Input for the first list
list1 = input("Enter elements of the first list separated by spaces: ").split()
# Input for the second list
list2 = input("Enter elements of the second list separated by spaces: ").split()

# Check if both lists are of equal size
if len(list1) != len(list2):
    print("Error: The lists must be of equal size.")
else:
    # Initialize a variable to track the index of the first difference
    differing_index = -1

    # Loop through the elements of both lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differing_index = i
            break  # Exit the loop as we found the first difference

    # Check if a difference was found
    if differing_index == -1:
        print("The lists are identical.")
    else:
        print(f"The first differing index is: {differing_index}")
