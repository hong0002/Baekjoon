# 입력 받기
n = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(n)]

# 각 문제에 대해 단순한지 여부 판단하기
results = []
for i, f in tasks:
    if (i <= 1 and f <= 2) or (i <= 2 and f <= 1):
        results.append("Yes")
    else:
        results.append("No")

# 결과 출력하기
for result in results:
    print(result)
