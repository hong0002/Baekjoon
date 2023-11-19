# 입력 받기
N, M = map(int, input().split())

# 채울 수 있는 타일의 최댓값 계산
# 경우 1: 2×1 크기의 타일로 채우는 경우
max_tiles_case1 = (N // 2) * M + (N % 2) * (M // 2)

# 경우 2: 1×2 크기의 타일로 채우는 경우
max_tiles_case2 = (M // 2) * N + (M % 2) * (N // 2)

# 두 경우 중에서 더 큰 값을 선택
result = max(max_tiles_case1, max_tiles_case2)

# 결과 출력
print(result)
