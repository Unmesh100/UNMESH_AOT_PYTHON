import numpy as np
import matplotlib.pyplot as plt

# Function to get user input for the range of points
def get_user_input():
    try:
        x_min = float(input("Enter the minimum x-coordinate value: "))
        x_max = float(input("Enter the maximum x-coordinate value: "))
        y_min = float(input("Enter the minimum y-coordinate value: "))
        y_max = float(input("Enter the maximum y-coordinate value: "))

        if x_min >= x_max or y_min >= y_max:
            print("Invalid input. Ensure that min values are less than max values.")
            return None, None, None, None

        return x_min, x_max, y_min, y_max
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None, None

# Main code
x_min, x_max, y_min, y_max = get_user_input()

if x_min is not None:
    # Generate 30 random 2D points within the specified range
    x_points = np.random.uniform(x_min, x_max, 30)
    y_points = np.random.uniform(y_min, y_max, 30)

    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_points, y_points, color='blue', marker='o', edgecolor='k')
    plt.title('Scatter Plot of Random 2D Points')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.axhline(0, color='gray', lw=0.5, ls='--')
    plt.axvline(0, color='gray', lw=0.5, ls='--')
    plt.grid()
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.show()
