import random

# Taking user input for matrix size and range of random integers
try:
    rows = int(input("Enter the number of rows for the matrix (e.g., 3 for a 3x3 matrix): "))
    cols = int(input("Enter the number of columns for the matrix (e.g., 3 for a 3x3 matrix): "))
    lower_bound = int(input("Enter the lower bound for random integers: "))
    upper_bound = int(input("Enter the upper bound for random integers: "))
    
    # Create a matrix with random integers
    matrix = [[random.randint(lower_bound, upper_bound) for _ in range(cols)] for _ in range(rows)]
    
    # Display the matrix
    print(f"\n{rows}x{cols} Matrix:")
    for row in matrix:
        print(row)

    # Calculate and print the main diagonal elements
    main_diagonal = [matrix[i][i] for i in range(min(rows, cols))]
    main_diagonal_sum = sum(main_diagonal)
    
    # Calculate and print the anti-diagonal elements
    anti_diagonal = [matrix[i][cols - 1 - i] for i in range(min(rows, cols))]
    anti_diagonal_sum = sum(anti_diagonal)
    
    print("\nMain Diagonal Elements:", main_diagonal)
    print("Sum of Main Diagonal Elements:", main_diagonal_sum)
    
    print("\nAnti-Diagonal Elements:", anti_diagonal)
    print("Sum of Anti-Diagonal Elements:", anti_diagonal_sum)

except ValueError:
    print("Invalid input. Please enter valid integers.")
