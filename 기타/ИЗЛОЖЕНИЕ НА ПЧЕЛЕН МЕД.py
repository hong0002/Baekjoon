from itertools import permutations

def honey():
    # Read the input
    A1, A2, A3 = map(int, input().split())  # Prices of the three types of honey
    B1, B2, B3 = map(int, input().split())  # Capacities of the three containers

    # List of prices and capacities
    prices = [A1, A2, A3]
    capacities = [B1, B2, B3]

    # Calculate the maximum profit using permutations
    max_profit = 0
    for perm in permutations(range(3)):
        # Calculate the profit for the current permutation
        profit = prices[perm[0]] * capacities[0] + prices[perm[1]] * capacities[1] + prices[perm[2]] * capacities[2]
        max_profit = max(max_profit, profit)
    
    # Output the maximum profit
    print(max_profit)

# Run the function
honey()
