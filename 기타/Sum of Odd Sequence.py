def calculate_odd_sum(N):
    # Calculate the number of terms (k)
    k = (N + 1) // 2
    # Return k squared
    return k * k

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N = int(input().strip())
    result = calculate_odd_sum(N)
    print(result)
