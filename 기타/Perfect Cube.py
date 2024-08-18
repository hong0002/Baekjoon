import sys
import bisect

# Precompute all perfect cubes up to 1254^3
max_val = 2000000000
i = 1
cubes = []
while True:
    cube = i**3
    if cube > max_val:
        break
    cubes.append(cube)
    i += 1

# Function to handle the input and perform the computation
def handle_cases():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for case_number in range(1, T + 1):
        A = int(data[idx])
        B = int(data[idx + 1])
        idx += 2
        
        # Find the number of cubes between A and B
        start = bisect.bisect_left(cubes, A)
        end = bisect.bisect_right(cubes, B)
        count = end - start
        
        results.append(f"Case #{case_number}: {count}")
    
    # Print all results
    sys.stdout.write("\n".join(results) + "\n")

# Call the function to handle the cases
handle_cases()
