def tower_of_hanoi(n, source, target, helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1
    # Recursive step to move n-1 disks from source to helper using target as helper
    steps = tower_of_hanoi(n - 1, source, helper, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    steps += 1
    # Move n-1 disks from helper to target using source as helper
    steps += tower_of_hanoi(n - 1, helper, target, source)
    return steps

# Taking user input for the number of disks
try:
    n = int(input("Enter the number of disks: "))
    if n <= 0:
        print("The number of disks must be a positive integer.")
    else:
        print(f"Solution for {n} disks:")
        total_steps = tower_of_hanoi(n, 'A', 'C', 'B')
        print(f"Total number of steps: {total_steps}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# The tower_of_hanoi function takes 3 parameters: n, source, target, and helper. n is the number of disks, source is the starting peg, target is the destination peg, and helper is the auxiliary peg.
# To calculate the number of steps for n disks, we can use the following formula: 2^n - 1 where n is the number of disks.
