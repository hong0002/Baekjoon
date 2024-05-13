# Read input values A and B from standard input
A, B = map(int, input().split())

# Calculate A+B and A-B
sum_result = A + B
diff_result = A - B

# Determine the maximum and minimum of the two results
max_value = max(sum_result, diff_result)
min_value = min(sum_result, diff_result)

# Print the maximum value on the first line
print(max_value)

# Print the minimum value on the second line
print(min_value)
