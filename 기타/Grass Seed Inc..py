import sys
input = sys.stdin.readline

def main():
    C = float(input().strip())      # 단위 면적당 씨앗 비용
    L = int(input().strip())        # 잔디밭 개수

    total_cost = 0.0
    for _ in range(L):
        w, l = map(float, input().split())
        total_cost += C * (w * l)

    # 소수점 이하 7자리까지 출력
    print(f"{total_cost:.7f}")

if __name__ == "__main__":
    main()
