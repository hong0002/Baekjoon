P, M, C = map(int, input().split())
X = int(input())

answer = float('inf')

for p in range(1, P + 1):
    for m in range(1, M + 1):
        for c in range(1, C + 1):
            value = (p + m) * (m + c)
            diff = abs(value - X)
            answer = min(answer, diff)

print(answer)
