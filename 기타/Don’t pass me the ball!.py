import math

def count_scoring_combinations(goal_scorer_jersey):
    # Total players to pick from is goal_scorer_jersey - 1
    n = goal_scorer_jersey - 1
    
    # We need to pick 3 players
    k = 3
    
    if n < k:
        # Not enough players to pick from
        return 0
    
    # Calculate the combinations using the formula for "n choose k"
    return math.comb(n, k)

# Read input
goal_scorer_jersey = int(input().strip())

# Compute the result
result = count_scoring_combinations(goal_scorer_jersey)

# Output the result
print(result)
