def find_latest_bus(N, X, buses):
    latest_time = -1  # 초기값을 -1로 설정
    
    for S, T in buses:
        if S + T <= X:
            if S > latest_time:
                latest_time = S
    
    return latest_time

# 입력 받기
N, X = map(int, input().split())
buses = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = find_latest_bus(N, X, buses)
print(result)
