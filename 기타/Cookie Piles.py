# 입력 받기
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# 결과 계산 및 출력
for N, A, D in test_cases:
    total_cookies = (N * (2 * A + (N - 1) * D)) // 2
    print(total_cookies)
