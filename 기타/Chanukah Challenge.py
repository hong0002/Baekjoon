# 데이터 세트 개수 입력 받기
P = int(input())

# 각 데이터 세트 처리
for _ in range(P):
    # 데이터 세트 번호와 일수 입력 받기
    K, N = map(int, input().split())
    
    # 총 필요한 촛불 수 계산
    total_candles = N * (N + 1) // 2 + N
    
    # 결과 출력
    print(K, total_candles)
