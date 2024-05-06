# Input
N, H = map(int, input().split())  # Number of rides, Carlitos' height
min_heights = list(map(int, input().split()))  # Minimum heights of each ride

# Count the number of rides Carlitos can enjoy
rides_count = 0
for height in min_heights:
    if height <= H:
        rides_count += 1

# Output the result
print(rides_count)
