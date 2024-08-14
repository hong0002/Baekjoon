N = int(input())

# x와 y를 최적으로 나눈 후 최대 조각 수 계산
x = N // 2
y = N - x

max_pieces = (x + 1) * (y + 1)
print(max_pieces)
