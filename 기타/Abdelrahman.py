def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N, M = map(int, data[i].split())
        # The maximum number of removable cables
        R = M - (N - 1)
        results.append(f"Case {i}: {R}")
    
    # Print all results
    for result in results:
        print(result)

# Run the solve function
solve()
