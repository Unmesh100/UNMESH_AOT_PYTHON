# Function to take user input for a 3x3 matrix
def input_matrix(name):
    print(f"Enter the elements for the {name} matrix (row by row):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 integers for each row.")
            return None
        matrix.append(row)
    return matrix

# Function to perform matrix multiplication
def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 result matrix
    for i in range(3):
        for j in range(3):
            for k in range(3):  # For the dot product
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Main code
matrix1 = input_matrix("first")
matrix2 = input_matrix("second")

if matrix1 is not None and matrix2 is not None:
    result_matrix = multiply_matrices(matrix1, matrix2)
    print("\nResultant Matrix after Multiplication:")
    for row in result_matrix:
        print(row)
