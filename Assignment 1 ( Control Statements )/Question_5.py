# Prompt the user to enter the student's average mark
average_mark = float(input("Enter the student's average mark: "))

# Check the student's grade based on the average mark
if average_mark >= 91 and average_mark <= 100:
    grade = "O"
elif average_mark >= 81 and average_mark <= 90:
    grade = "A+"
elif average_mark >= 71 and average_mark <= 80:
    grade = "A"
elif average_mark >= 61 and average_mark <= 70:
    grade = "B"
elif average_mark >= 51 and average_mark <= 60:
    grade = "C"
elif average_mark >= 41 and average_mark <= 50:
    grade = "D"
elif average_mark >= 33 and average_mark <= 40:
    grade = "E"
else:
    grade = "F"

# Display the student's grade
print("The student's grade is:", grade)