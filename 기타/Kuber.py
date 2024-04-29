def calculate_blocks(N):
    total_blocks = 0
    for i in range(1, N + 1):
        total_blocks += i**3
    return total_blocks

N = int(input())
result = calculate_blocks(N)
print(result)
