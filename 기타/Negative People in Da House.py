def minimum_initial_people(test_cases):
    results = []
    
    for case in test_cases:
        M = case['M']
        events = case['events']
        
        # Start by assuming no one is in the house
        people_in_house = 0
        minimum_people_needed = 0
        
        for P1, P2 in events:
            people_in_house += P1
            people_in_house -= P2
            
            # If people_in_house goes negative, update minimum_people_needed
            if people_in_house < 0:
                minimum_people_needed = max(minimum_people_needed, -people_in_house)
        
        results.append(minimum_people_needed)
    
    return results

# Reading input
T = int(input())
test_cases = []

for _ in range(T):
    M = int(input())
    events = []
    for _ in range(M):
        P1, P2 = map(int, input().split())
        events.append((P1, P2))
    test_cases.append({'M': M, 'events': events})

# Processing each test case
results = minimum_initial_people(test_cases)

# Output the results for each test case
for i, result in enumerate(results):
    print(result)
