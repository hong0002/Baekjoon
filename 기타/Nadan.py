# 입력 받기
K = int(input())  # 총 금액 K
N = int(input())  # 프로젝트의 수 N

# N개의 프로젝트에 최소로 분배해야 하는 금액의 합
min_sum = N * (N + 1) // 2

# 각 프로젝트에 분배할 금액 초기화 (1, 2, ..., N)
distribution = list(range(1, N + 1))

# 남은 금액
remaining = K - min_sum

# 남은 금액을 뒤에서부터 더해줌
index = N - 1
while remaining > 0:
    distribution[index] += 1
    remaining -= 1
    index -= 1
    if index < 0:
        index = N - 1

# 결과 출력
for amount in distribution:
    print(amount)
