# Cookie Shipping Calculator

# Constants
COOKIES_PER_BOX = 24
BOXES_PER_CONTAINER = 75

# Program Introduction
print("Cookie Shipping Calculator:")
print("---------------------------")

# Input total number of cookies
total_cookies = int(input("Enter the total number of cookies: "))

# Calculate number of full boxes
boxes_count = total_cookies // COOKIES_PER_BOX
leftover_cookies = total_cookies % COOKIES_PER_BOX

# Calculate number of full containers
containers_count = boxes_count // BOXES_PER_CONTAINER
leftover_boxes = boxes_count % BOXES_PER_CONTAINER

# Print results
print("\nShipping Details:")
print("----------------")
print(f"Total Cookies: {total_cookies}")
print(f"Cookies per Box: {COOKIES_PER_BOX}")
print(f"Boxes per Container: {BOXES_PER_CONTAINER}")

print("\nShipping Breakdown:")
print(f"Full Boxes: {boxes_count}")
print(f"Leftover Cookies: {leftover_cookies}")

print(f"\nFull Containers: {containers_count}")
print(f"Leftover Boxes: {leftover_boxes}")

# Additional information
print("\nNote:")
if leftover_cookies > 0:
    print(f"- {leftover_cookies} cookies could not be fully boxed")
if leftover_boxes > 0:
    print(f"- {leftover_boxes} boxes could not be fully containerized")