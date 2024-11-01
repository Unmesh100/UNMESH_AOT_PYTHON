def get_row_max(matrix):
    return [max(row) for row in matrix]

def get_col_min(matrix):
    return [min(col) for col in zip(*matrix)]

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix.append(row)
    
    row_max = get_row_max(matrix)
    col_min = get_col_min(matrix)
    
    print("Row-wise maximum elements:", row_max)
    print("Column-wise minimum elements:", col_min)

if __name__ == "__main__":
    main()
