import math

def calculate_distance_and_speed(diameter, revolutions, time_seconds):
    if revolutions == 0:
        return None
    
    # Calculate the distance in miles
    distance_inches = math.pi * diameter * revolutions
    distance_miles = distance_inches / 63360
    
    # Calculate the time in hours
    time_hours = time_seconds / 3600
    
    # Calculate the average speed in miles per hour
    average_speed_mph = distance_miles / time_hours
    
    return distance_miles, average_speed_mph

def main():
    trip_number = 1
    
    while True:
        data = input().strip()
        if not data:
            break
        
        diameter, revolutions, time_seconds = map(float, data.split())
        revolutions = int(revolutions)
        
        if revolutions == 0:
            break
        
        result = calculate_distance_and_speed(diameter, revolutions, time_seconds)
        if result:
            distance, speed = result
            print(f"Trip #{trip_number}: {distance:.2f} {speed:.2f}")
            trip_number += 1

# Call the main function to start the program
main()
