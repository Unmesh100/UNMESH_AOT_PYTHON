# Interest Calculator Program

# Print program introduction
print("Interest Calculator:")
print("--------------------")

# Input principal amount
principal = float(input("Enter the principal amount: "))

# Input interest rate
rate = float(input("Enter the annual interest rate (in %): "))

# Input time period
time = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest = (principal * time * rate) / 100
total_simple_amount = principal + simple_interest

# Calculate Compound Interest
compound_interest = principal * ((1 + rate / 100) ** time - 1)
total_compound_amount = principal + compound_interest

# Print results
print("\nResults:")
print("--------")
print(f"Principal Amount: ₹{principal:.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time Period: {time} years")

print("\nSimple Interest Calculation:")
print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Total Amount (Simple Interest): ₹{total_simple_amount:.2f}")

print("\nCompound Interest Calculation:")
print(f"Compound Interest: ₹{compound_interest:.2f}")
print(f"Total Amount (Compound Interest): ₹{total_compound_amount:.2f}")

# Calculate the difference
interest_difference = total_compound_amount - total_simple_amount
print(f"\nDifference between Compound and Simple Interest: ₹{interest_difference:.2f}")