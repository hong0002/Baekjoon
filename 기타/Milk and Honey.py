def main():
    import sys
    input = sys.stdin.readline

    # 첫 줄 입력: M, H
    M, H = map(int, input().split())
    # 두 번째 줄 입력: 밭의 개수 N
    N = int(input())
    
    total_happiness = 0
    for _ in range(N):
        C, B = map(int, input().split())
        # 각 밭에서 최대 행복 계산: 소를 키웠을 때와 벌을 키웠을 때 중 큰 값 선택
        total_happiness += max(C * M, B * H)
    
    print(total_happiness)

if __name__ == "__main__":
    main()
