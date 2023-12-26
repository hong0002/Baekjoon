# Read input
D, H, M = map(int, input().split())

# Constants for the start time
start_day = 11
start_hour = 11
start_minute = 11

# Calculate the total minutes for both the start and end times
start_total_minutes = (start_day - 11) * 24 * 60 + start_hour * 60 + start_minute
end_total_minutes = (D - 11) * 24 * 60 + H * 60 + M

# Calculate the difference in minutes
minutes_spent = end_total_minutes - start_total_minutes

# Check if the ending time is earlier than the starting time
if minutes_spent < 0:
    print(-1)
else:
    print(minutes_spent)
