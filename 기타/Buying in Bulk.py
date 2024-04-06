# Function to compute the total cost for a customer
def compute_total_cost(items, price):
    if items == 1:
        return items * price
    else:
        return price + (items - 1) * (price - 2)

# Main function
def main():
    n = int(input())  # Number of customers
    for _ in range(n):
        items, price = map(int, input().split())
        total_cost = compute_total_cost(items, price)
        print(items, price)
        print(total_cost)

if __name__ == "__main__":
    main()
