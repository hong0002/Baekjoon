# 입력 받기
N = int(input())
K = input()

# 짝수와 홀수 개수 세기
even_count = 0
odd_count = 0

for digit in K:
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 결과 출력
if even_count > odd_count:
    print(0)
elif odd_count > even_count:
    print(1)
else:
    print(-1)
