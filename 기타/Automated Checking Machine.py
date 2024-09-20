def are_connectors_compatible():
    # Read input for the two connectors
    connector1 = list(map(int, input().strip().split()))
    connector2 = list(map(int, input().strip().split()))
    
    # Check for compatibility
    for i in range(5):
        if connector1[i] + connector2[i] != 1:
            print("N")
            return
    
    # If all checks pass, they are compatible
    print("Y")

# Execute the function
are_connectors_compatible()
