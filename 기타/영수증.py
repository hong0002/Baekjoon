def find_missing_price():
    total_price = int(input().strip())           # 10권의 총 가격
    known_sum = sum(int(input().strip()) for _ in range(9))  # 읽을 수 있는 9권 가격의 합
    print(total_price - known_sum)               # 남은 1권의 가격

if __name__ == "__main__":
    find_missing_price()
