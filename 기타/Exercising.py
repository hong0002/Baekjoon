def process_pedometer_data():
    user_count = 1

    while True:
        # Read the stride length
        L = int(input().strip())
        
        # Exit condition
        if L == 0:
            break
        
        # Read the number of entries for the user
        N = int(input().strip())
        
        print(f"User {user_count}")
        
        # Process each step entry
        for _ in range(N):
            steps = int(input().strip())
            # Calculate distance in kilometers
            distance_km = (steps * L) / 100000
            # Print the distance with 5 decimal places
            print(f"{distance_km:.5f}")
        
        # Move to the next user
        user_count += 1

# Execute the function to process the data
process_pedometer_data()
