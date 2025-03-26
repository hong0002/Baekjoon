# 입력받은 N
N = int(input())

count = 0
# A와 B의 범위는 1부터 500까지
for A in range(1, 501):
    for B in range(1, A+1):  # B는 1 <= B <= A
        if A * A - B * B == N:
            count += 1

print(count)
