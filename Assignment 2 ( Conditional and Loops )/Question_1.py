# Print the program introduction
print("Welcome to the Item Cost Calculator!")
print("------------------------------------")

# Ask the user to enter the number of items they are buying
num_items = int(input("Enter the number of items you are buying: "))

# Calculate the total cost based on the number of items
if num_items < 10:
    cost_per_item = 120
    total_cost = num_items * cost_per_item
    print(f"The total cost for {num_items} items is Rs {total_cost}")
elif num_items >= 10 and num_items < 100:
    cost_per_item = 100
    total_cost = num_items * cost_per_item
    print(f"The total cost for {num_items} items is Rs {total_cost}")
else:
    cost_per_item = 70
    total_cost = num_items * cost_per_item
    print(f"The total cost for {num_items} items is Rs {total_cost}")