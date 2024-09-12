def compute_missing_values():
    import sys
    input = sys.stdin.read
    lines = input().strip().split('\n')

    for line in lines:
        # Read each line
        l, w, a = map(int, line.split())
        
        # Stop processing when we reach the terminating line "0 0 0"
        if l == 0 and w == 0 and a == 0:
            break
        
        # Determine which value is missing and compute it
        if l == 0:
            l = a // w
        elif w == 0:
            w = a // l
        elif a == 0:
            a = l * w
        
        # Print the corrected line
        print(f"{l} {w} {a}")

# Run the function
compute_missing_values()
