# Read input values
t1, m1, t2, m2 = map(int, input().split())

# Convert the start and end times to minutes since the beginning of the day
start_minutes = t1 * 60 + m1
end_minutes = t2 * 60 + m2

# Calculate the total duration in minutes
if end_minutes >= start_minutes:
    total_minutes = end_minutes - start_minutes
else:
    total_minutes = (24 * 60 - start_minutes) + end_minutes

# Calculate the number of full laps
full_laps = total_minutes // 30

# Output the result
print(total_minutes, full_laps)
