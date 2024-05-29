import math

def minimum_cost(S, A, B):
    if A >= S:
        return 250
    else:
        additional_height_needed = S - A
        additional_layers = math.ceil(additional_height_needed / B)
        total_cost = 250 + 100 * additional_layers
        return total_cost

# Example input
S = int(input())
A = int(input())
B = int(input())

# Calculate and print the minimum cost
print(minimum_cost(S, A, B))
