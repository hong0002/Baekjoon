def calculate_repayment(n, s, d, ships):
    total_ducats = 0
    for distance, value in ships:
        time_to_reach = distance / s
        if time_to_reach <= d:
            total_ducats += value
    return total_ducats

def main():
    K = int(input())
    
    for dataset in range(1, K+1):
        n, s, d = map(int, input().split())
        ships = [tuple(map(int, input().split())) for _ in range(n)]

        repayment = calculate_repayment(n, s, d, ships)

        print(f"Data Set {dataset}:")
        print(repayment)
        print()

if __name__ == "__main__":
    main()
