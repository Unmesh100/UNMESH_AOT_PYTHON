def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    # Get user input
    user_input = input("Enter a list of numbers separated by spaces: ")
    # Convert input string to a list of integers
    num_list = [int(num) for num in user_input.split()]
    
    # Call the bubble sort function
    sorted_list = bubble_sort(num_list)
    
    print("Sorted list:", sorted_list)
