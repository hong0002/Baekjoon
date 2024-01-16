# Pepper SHU values
shu_values = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

# Function to calculate total spiciness
def calculate_spiciness(N, peppers):
    total_spiciness = sum(shu_values[pepper] for pepper in peppers)
    return total_spiciness

# Input
N = int(input())
peppers = [input().strip() for _ in range(N)]

# Output
print(calculate_spiciness(N, peppers))
