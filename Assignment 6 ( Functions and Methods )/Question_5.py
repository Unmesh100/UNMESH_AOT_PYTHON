def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid index to avoid overflow

        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found, return the index

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    # Get user input
    user_input = input("Enter a sorted list of numbers separated by spaces: ")
    # Convert input string to a list of integers
    num_list = [int(num) for num in user_input.split()]

    target = int(input("Enter the number to search for: "))

    # Call the binary search function
    result = binary_search(num_list, target)

    if result != -1:
        print(f"Number {target} found at index {result}.")
    else:
        print(f"Number {target} not found in the list.")
