def find_factors(n):
    """ Returns a sorted list of all factors of n """
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    P = int(data[0])
    Q = int(data[1])
    
    factors_P = find_factors(P)
    factors_Q = find_factors(Q)
    
    # Create and print all combinations of factors of P and Q
    results = []
    for p in factors_P:
        for q in factors_Q:
            results.append(f"{p} {q}")
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
