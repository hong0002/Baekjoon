# Read input depth readings
depth_readings = [int(input()) for _ in range(4)]

# Check for Fish Rising
if depth_readings[0] < depth_readings[1] < depth_readings[2] < depth_readings[3]:
    print("Fish Rising")
# Check for Fish Diving
elif depth_readings[0] > depth_readings[1] > depth_readings[2] > depth_readings[3]:
    print("Fish Diving")
# Check for Constant Depth
elif depth_readings[0] == depth_readings[1] == depth_readings[2] == depth_readings[3]:
    print("Fish At Constant Depth")
# No Fish
else:
    print("No Fish")
