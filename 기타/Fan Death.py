def sum_of_divisors(n):
    total_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:  # i is a divisor of n
            total_sum += i
    return total_sum

# Read input
n = int(input().strip())

# Calculate the sum of divisors
divisor_sum = sum_of_divisors(n)

# Apply the transformation
result = (divisor_sum * 5) - 24

# Output the result
print(result)
