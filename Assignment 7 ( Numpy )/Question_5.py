import numpy as np

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix.append(row)
    
    np_matrix = np.array(matrix)
    
    row_max = np.max(np_matrix, axis=1)
    col_min = np.min(np_matrix, axis=0)
    
    print("Row-wise maximum elements:", row_max)
    print("Column-wise minimum elements:", col_min)

if __name__ == "__main__":
    main()
