# Function to determine whether to choose Whole pizza or Slice of pizza
def maximize_pizza_value(area_price, radius_price):
    pizza_slice_value = area_price[0] / area_price[1]  # Area per dollar for pizza slice
    whole_pizza_value = (3.141592653589793 * radius_price[0]**2) / radius_price[1]  # Area per dollar for whole pizza

    return "Whole pizza" if whole_pizza_value > pizza_slice_value else "Slice of pizza"

# Number of datasets
n = int(input())

# Process each dataset
for _ in range(n):
    # Input for each dataset
    area_price = list(map(int, input().split()))
    radius_price = list(map(int, input().split()))

    # Output the result for each dataset
    print(maximize_pizza_value(area_price, radius_price))
