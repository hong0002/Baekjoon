def main():
    import sys
    input = sys.stdin.readline

    # 입력: 카드의 개수 N, 예측 카드 P, 단계의 수 S
    N, P, S = map(int, input().split())
    
    # 남아있는 카드의 집합 (초기에는 1부터 N까지 모두 있음)
    available = set(range(1, N + 1))
    
    for _ in range(S):
        data = list(map(int, input().split()))
        m = data[0]
        chosen = set(data[1:])
        
        # 예측 카드 P가 선택된 카드에 있으면 선택된 카드를 유지 (KEEP)
        if P in chosen:
            print("KEEP")
            available = chosen  # 남은 카드는 선택된 카드들로 업데이트
        else:
            print("REMOVE")
            available -= chosen  # 남은 카드에서 선택된 카드를 제거

if __name__ == '__main__':
    main()
