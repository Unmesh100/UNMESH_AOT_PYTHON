def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def find_prime_sums(target, primes, curr_sum=0, combo=None, start=0):
    combo = combo or []
    if curr_sum == target:
        return [combo]
    return [new_combo 
            for i in range(start, len(primes)) 
            if curr_sum + primes[i] <= target 
            for new_combo in find_prime_sums(target, primes, curr_sum + primes[i], 
                                           combo + [primes[i]], i)]

def main():
    try:
        limit = int(input("Enter upper limit: "))
        primes = [n for n in range(2, limit + 1) if is_prime(n)]
        
        for prime in primes:
            smaller_primes = [p for p in primes if p < prime]
            combinations = find_prime_sums(prime, smaller_primes)
            
            if combinations:
                print(f"\n{prime} =")
                for combo in combinations:
                    print(" + ".join(map(str, combo)))
                    
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()