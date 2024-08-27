def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # First line: number of rooms `n` and cost per square meter `c`
    n, c = map(int, data[0].split())
    
    # Initialize totals
    total_area = 0
    total_bedroom_area = 0
    reduced_total_area = 0
    
    # Process each room
    for i in range(1, n + 1):
        room_data = data[i].split()
        area = int(room_data[0])
        room_type = room_data[1]
        
        # Add to total area
        total_area += area
        
        # Add to bedroom area if it's a bedroom
        if room_type == "bedroom":
            total_bedroom_area += area
        
        # Calculate part of reduced area
        if room_type == "balcony":
            reduced_total_area += area / 2.0
        else:
            reduced_total_area += area
    
    # Calculate the cost of the flat
    cost_of_flat = reduced_total_area * c
    
    # Print results
    print(total_area)
    print(total_bedroom_area)
    print(f"{cost_of_flat:.6f}")

if __name__ == "__main__":
    main()
