import numpy as np

# Function to take user input for a 3x3 matrix
def input_matrix(name):
    print(f"Enter the elements for {name} matrix (row by row):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 integers for each row.")
            return None
        matrix.append(row)
    return np.array(matrix)

# Main code
matrix1 = input_matrix("first")
matrix2 = input_matrix("second")

if matrix1 is not None and matrix2 is not None:
    result_matrix = matrix1 + matrix2  # Add the two matrices
    print("\nResultant Matrix after Addition:")
    print(result_matrix)
