def collatz_steps(N):
    steps = 0
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
        steps += 1
    return steps

# Read the input
N = int(input())

# Calculate the number of steps and print the result
print(collatz_steps(N))
