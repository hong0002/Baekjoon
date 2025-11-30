import sys

def main():
    low, high = 1, 10
    dishonest = False

    while True:
        line = sys.stdin.readline().strip()
        if not line:  # 입력 끝 안전 처리
            break

        guess = int(line)
        if guess == 0:
            break  # 전체 입력 끝

        response = sys.stdin.readline().strip()

        if response == "too low":
            low = max(low, guess + 1)
        elif response == "too high":
            high = min(high, guess - 1)
        elif response == "right on":
            # 마지막 판단
            if dishonest or not (low <= guess <= high):
                print("Stan is dishonest")
            else:
                print("Stan may be honest")
            # 다음 게임을 위해 초기화
            low, high = 1, 10
            dishonest = False
            continue

        # 범위가 말이 안 되면 이미 거짓말
        if low > high:
            dishonest = True

if __name__ == "__main__":
    main()
