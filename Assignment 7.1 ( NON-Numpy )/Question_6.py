# Function to add two matrices
def add_matrices(A, B):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

# Function to subtract two matrices
def subtract_matrices(A, B):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] - B[i][j]
    return result

# Function to multiply two matrices
def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Input matrices from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of the first matrix:")
A = [[complex(input(f"Element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Enter the elements of the second matrix:")
B = [[complex(input(f"Element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Addition of the matrices:")
print_matrix(add_matrices(A, B))

print("Subtraction of the matrices:")
print_matrix(subtract_matrices(A, B))

print("Multiplication of the matrices:")
print_matrix(multiply_matrices(A, B))
