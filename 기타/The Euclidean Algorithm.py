def original_euclidean_steps(A, B):
    steps = 0
    while A != B:
        if A > B:
            A = A - B
        else:
            B = B - A
        steps += 1
    return steps

# Read input
A, B = map(int, input().strip().split())

# Calculate the number of steps in the original Euclidean algorithm
result = original_euclidean_steps(A, B)

# Print the result
print(result)
