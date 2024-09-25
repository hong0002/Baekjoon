def calculate_hamming_distance(v, u):
    # Count the number of positions where v[i] != u[i]
    return sum(1 for v_i, u_i in zip(v, u) if v_i != u_i)

def main():
    # Read number of test cases
    T = int(input())
    
    results = []
    
    for _ in range(T):
        # Read dimension of the vectors
        n = int(input())
        
        # Read the first vector
        v = list(map(int, input().split()))
        
        # Read the second vector
        u = list(map(int, input().split()))
        
        # Calculate Hamming distance
        distance = calculate_hamming_distance(v, u)
        
        # Store the result
        results.append(distance)
    
    # Print all results
    for result in results:
        print(result)

# Run the main function
main()
