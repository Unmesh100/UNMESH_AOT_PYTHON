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
    return matrix

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 result matrix
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

# Main code
matrix1 = input_matrix("first")
matrix2 = input_matrix("second")

if matrix1 is not None and matrix2 is not None:
    result_matrix = add_matrices(matrix1, matrix2)
    print("\nResultant Matrix after Addition:")
    for row in result_matrix:
        print(row)
