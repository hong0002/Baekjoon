def count_domino_dots(N):
    total_dots = 0
    for i in range(N + 1):
        for j in range(i, N + 1):
            total_dots += i + j
    return total_dots

# 입력 받기
N = int(input())

# 결과 출력
print(count_domino_dots(N))
