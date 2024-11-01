# Simple Years to Time Calculator

# Ask user for input
print("Years to Time Calculator:")
print("-------------------------")

# Get number of years from user
years = int(input("Enter the number of years: "))

# Calculate total days (basic calculation)
total_days = years * 365

# Simple leap year check
# Add extra day for every 4 years
leap_days = years // 4

# Total days including leap days
total_days = total_days + leap_days

# Calculate other time units
total_hours = total_days * 24
total_minutes = total_hours * 60
total_seconds = total_minutes * 60

# Print results
print("\nTime Breakdown:")
print(f"Total Days: {total_days}")
print(f"Total Hours: {total_hours}")
print(f"Total Minutes: {total_minutes}")
print(f"Total Seconds: {total_seconds}")

# Leap year identification (simple version)
print("\nLeap Years:")
for year in range(1, years + 1):
    if year % 4 == 0:
        print(year, end=" ")