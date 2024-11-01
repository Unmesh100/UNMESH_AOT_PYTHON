def kth_largest_factor(N, k):
    # List to store factors of N
    factors = []
    
    # Find all factors of N
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            factors.append(i)
            # Add the corresponding factor pair if it's different
            if i != N // i:
                factors.append(N // i)
    
    # Sort factors in descending order
    factors.sort(reverse=True)
    
    # Check if k is within the range of the number of factors
    if k <= len(factors):
        return factors[k - 1]
    else:
        return f"The value of k ({k}) exceeds the number of factors of N ({N})."

# Taking user input
try:
    N = int(input("Enter a positive integer N: "))
    k = int(input("Enter a positive integer k: "))
    
    if N <= 0 or k <= 0:
        print("Both N and k must be positive integers.")
    else:
        result = kth_largest_factor(N, k)
        print(f"The {k}-th largest factor of {N} is: {result}")
except ValueError:
    print("Invalid input. Please enter positive integers for N and k.")
