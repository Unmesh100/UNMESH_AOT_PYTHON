import itertools

# Input for the list of elements
input_list = input("Enter elements of the list separated by spaces: ").split()

# Displaying permutations
print("\nPermutations:")
# Generate all permutations of the list
for perm in itertools.permutations(input_list):
    print(perm)

# Displaying combinations
print("\nCombinations:")
# Generate combinations of different lengths
for r in range(1, len(input_list) + 1):  # r varies from 1 to the length of the list
    print(f"\nCombinations of length {r}:")
    for combo in itertools.combinations(input_list, r):
        print(combo)
