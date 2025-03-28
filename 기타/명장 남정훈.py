def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L, R, A = map(int, input_data)
    
    # 두 진영의 차이를 계산합니다.
    diff = abs(L - R)
    
    # 양발잡이 선수를 배분할 때
    if A <= diff:
        # A가 차이 이하라면 모두 작은 쪽에 배분
        result = 2 * (min(L, R) + A)
    else:
        # 차이를 맞춘 후 남은 양발잡이 선수
        remaining = A - diff
        # 남은 선수들은 두 진영에 균등하게 나눕니다.
        result = 2 * (max(L, R) + remaining // 2)
    
    print(result)

if __name__ == "__main__":
    solve()
