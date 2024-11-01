import numpy as np

# Taking user input for matrix size and range of random integers
try:
    rows = int(input("Enter the number of rows for the matrix (e.g., 3 for a 3x3 matrix): "))
    cols = int(input("Enter the number of columns for the matrix (e.g., 3 for a 3x3 matrix): "))
    lower_bound = int(input("Enter the lower bound for random integers: "))
    upper_bound = int(input("Enter the upper bound for random integers: "))
    
    # Create a matrix with random integers
    matrix = np.random.randint(lower_bound, upper_bound + 1, (rows, cols))
    
    # Display the matrix
    print(f"\n{rows}x{cols} Matrix:")
    print(matrix)

    # Calculate and print the main diagonal elements
    main_diagonal = np.diagonal(matrix)
    main_diagonal_sum = np.sum(main_diagonal)
    
    # Calculate and print the anti-diagonal elements
    anti_diagonal = np.fliplr(matrix).diagonal()
    anti_diagonal_sum = np.sum(anti_diagonal)

    print("\nMain Diagonal Elements:", main_diagonal)
    print("Sum of Main Diagonal Elements:", main_diagonal_sum)
    
    print("\nAnti-Diagonal Elements:", anti_diagonal)
    print("Sum of Anti-Diagonal Elements:", anti_diagonal_sum)

except ValueError:
    print("Invalid input. Please enter valid integers.")
