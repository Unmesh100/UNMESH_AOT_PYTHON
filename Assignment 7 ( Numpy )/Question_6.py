import numpy as np

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter the elements of the first matrix:")
    A = np.array([[complex(input(f"Element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

    print("Enter the elements of the second matrix:")
    B = np.array([[complex(input(f"Element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

    print("Addition of the matrices:")
    print(A + B)

    print("Subtraction of the matrices:")
    print(A - B)

    print("Multiplication of the matrices:")
    print(np.dot(A, B))

if __name__ == "__main__":
    main()
