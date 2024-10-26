from itertools import permutations

# 입력을 받아들입니다.
a, b, c, d = map(int, input().split())

# 가능한 모든 순열에 대해 계산합니다.
min_value = float('inf')
best_permutation = None

for perm in permutations([a, b, c, d]):
    # perm[0] / perm[1] + perm[2] / perm[3]의 값을 계산
    value = perm[0] / perm[1] + perm[2] / perm[3]
    # 최소값을 갱신합니다.
    if value < min_value:
        min_value = value
        best_permutation = perm

# 최소화된 결과를 출력합니다.
print(*best_permutation)
