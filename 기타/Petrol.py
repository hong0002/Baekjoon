def calculate_petrol_cost(petrol_used, quota_left):
    total_quota = 60 + quota_left  # Total quota available for the next month
    excess_petrol = max(0, petrol_used - total_quota)  # Calculate excess petrol

    # Calculate the cost based on the given conditions
    cost = min(petrol_used, total_quota) * 1500 + excess_petrol * 3000

    return cost

def main():
    # 입력 받기
    petrol_used = int(input())
    quota_left = int(input())

    # 결과 출력
    result = calculate_petrol_cost(petrol_used, quota_left)
    print(result)

if __name__ == "__main__":
    main()
