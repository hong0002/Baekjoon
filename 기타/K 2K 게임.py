N, K = map(int, input().split())
f_K = K % 10
f_2K = (2 * K) % 10
result = []
for x in range(1, N + 1):
    if x % 10 != f_K and x % 10 != f_2K:
        result.append(x)
print(len(result))  # 조건을 만족하는 수의 개수 출력
if result:
    print(" ".join(map(str, result)))  # 조건을 만족하는 수들을 공백으로 구분해 출력
else:
    print()  # 조건을 만족하는 수가 없다면 빈 줄 출력
