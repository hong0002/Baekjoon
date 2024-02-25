# Function to calculate charges for a customer
def calculate_charges(rate_first_1000, rate_additional, energy_consumption):
    if energy_consumption <= 1000:
        return energy_consumption * rate_first_1000
    else:
        additional_usage = energy_consumption - 1000
        return 1000 * rate_first_1000 + additional_usage * rate_additional

# Read the rates
rate_first_1000, rate_additional = map(int, input().split())

# Read the number of customers
n = int(input())

# Process each customer
for _ in range(n):
    # Read the customer's energy consumption
    energy_consumption = int(input())

    # Calculate and print the charges
    charges = calculate_charges(rate_first_1000, rate_additional, energy_consumption)
    print(f"{energy_consumption} {charges}")
