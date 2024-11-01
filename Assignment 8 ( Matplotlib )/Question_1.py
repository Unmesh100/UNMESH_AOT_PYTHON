import random
import matplotlib.pyplot as plt

# Function to take user input for the number of months and bill range
def get_user_input():
    try:
        # Get the number of months (default is 12)
        months_count = int(input("Enter the number of months (e.g., 12 for a year): "))
        
        # Get the minimum and maximum values for the electricity bill
        min_bill = float(input("Enter the minimum electricity bill amount: "))
        max_bill = float(input("Enter the maximum electricity bill amount: "))

        if months_count <= 0 or min_bill < 0 or max_bill <= min_bill:
            print("Invalid input. Please ensure the number of months is positive and the bill range is valid.")
            return None, None, None
        
        return months_count, min_bill, max_bill
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None

# Function to generate random monthly electricity bills
def generate_bills(months_count, min_bill, max_bill):
    bills = [random.uniform(min_bill, max_bill) for _ in range(months_count)]
    return bills

# Main code
months_count, min_bill, max_bill = get_user_input()

if months_count is not None:
    # Generate the months and bills
    months = [f'Month {i+1}' for i in range(months_count)]
    bills = generate_bills(months_count, min_bill, max_bill)

    # Print the generated bills
    print("\nMonthly Electricity Bills:")
    for month, bill in zip(months, bills):
        print(f"{month}: ${bill:.2f}")

    # Plotting the data

    # Line chart
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.plot(months, bills, marker='o', linestyle='-', color='b')
    plt.title('Monthly Electricity Bills (Line Chart)')
    plt.xlabel('Months')
    plt.ylabel('Electricity Bill ($)')
    plt.xticks(rotation=45)
    plt.grid()

    # Bar chart
    plt.subplot(1, 3, 2)
    plt.bar(months, bills, color='orange')
    plt.title('Monthly Electricity Bills (Bar Chart)')
    plt.xlabel('Months')
    plt.ylabel('Electricity Bill ($)')
    plt.xticks(rotation=45)
    plt.grid()

    # Pie chart
    plt.subplot(1, 3, 3)
    plt.pie(bills, labels=months, autopct='%1.1f%%', startangle=140)
    plt.title('Monthly Electricity Bills (Pie Chart)')

    plt.tight_layout()  # Adjust subplots to fit into figure area.
    plt.show()