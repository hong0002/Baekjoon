# Function to calculate the total earnings for each data set
def calculate_earnings(data):
    total_earnings = 0
    for item in data:
        name, quantity, price = item
        total_earnings += quantity * price
    return total_earnings

# Function to format the earnings in dollars
def format_earnings(earnings):
    return '${:.2f}'.format(earnings)

# Main function
def main():
    # Number of data sets
    n = int(input())

    # Iterate through each data set
    for _ in range(n):
        # Number of items in the data set
        x = int(input())

        # Initialize list to store data for this data set
        data = []

        # Read and process each item
        for _ in range(x):
            name, quantity, price = input().split()
            quantity = int(quantity)
            price = float(price)
            data.append((name, quantity, price))

        # Calculate total earnings for this data set
        earnings = calculate_earnings(data)

        # Output the earnings
        print(format_earnings(earnings))

if __name__ == "__main__":
    main()
