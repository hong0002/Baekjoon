def time_before_45_minutes(T, times):
    results = []
    
    for i in range(T):
        H, M = times[i]
        
        # Calculate the new minutes and possibly adjust hours
        new_minutes = M - 45
        new_hours = H
        if new_minutes < 0:
            new_minutes += 60
            new_hours -= 1
            
        # If hour is negative, wrap around to the last hour of the day
        if new_hours < 0:
            new_hours = 23
        
        # Append the result formatted as requested
        results.append(f"Case #{i + 1}: {new_hours} {new_minutes}")
    
    return results

# Read input
T = int(input().strip())
times = []

for _ in range(T):
    H, M = map(int, input().strip().split())
    times.append((H, M))

# Process the time calculations
results = time_before_45_minutes(T, times)

# Output the results
for result in results:
    print(result)
