# 입력 받은 자연수 C(1)을 시작으로 수열을 생성합니다.
n = int(input().strip())
count = 1  # C(1)을 첫 번째 항으로 간주

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count += 1

print(count)
