# 입력 받기
N, M = map(int, input().split())  # N: 바구니의 수, M: 작업의 수

# 바구니 리스트 초기화 (각 바구니에 0으로 시작)
baskets = [0] * N

# M번의 작업 수행
for _ in range(M):
    i, j, k = map(int, input().split())
    # i번부터 j번 바구니까지 k번 공을 넣음
    for idx in range(i-1, j):  # 인덱스는 0부터 시작하므로 i-1부터 j-1까지
        baskets[idx] = k

# 결과 출력
print(*baskets)
