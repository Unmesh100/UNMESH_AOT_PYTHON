# Get input from user
print("Enter heights (space-separated integers):")
try:
    height = list(map(int, input().strip().split()))
except ValueError:
    print("Invalid input! Please enter integers only.")
    exit()

# Check constraints
n = len(height)
if not (1 <= n <= 2 * 10**4):
    print("Invalid input: Length should be between 1 and 20000")
    exit()

if not all(0 <= h <= 10**5 for h in height):
    print("Invalid input: Heights should be between 0 and 100000")
    exit()

# If length is less than 3, no water can be trapped
if len(height) < 3:
    print("Output: 0")
    exit()

# Initialize variables
total_water = 0
n = len(height)

# Find the maximum height to the left of each position
left_max = [0] * n
left_max[0] = height[0]
for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i])

# Find the maximum height to the right of each position
right_max = [0] * n
right_max[n-1] = height[n-1]
for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i])

# Calculate water trapped at each position
for i in range(n):
    # Water at current position = min(max_left, max_right) - current_height
    water = min(left_max[i], right_max[i]) - height[i]
    if water > 0:
        total_water += water

# Print result
print(f"\nInput: height = {height}")
print(f"Output: {total_water}")