n = int(input())

# Calculate n!
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Extract the last digit of n!
last_digit = factorial % 10

print(last_digit)
