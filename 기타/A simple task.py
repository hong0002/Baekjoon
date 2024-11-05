# 입력 받기
n = int(input().strip())

# p와 o 초기화
p = 0

# 2로 나눌 수 있는 만큼 나누기
while n % 2 == 0:
    n //= 2
    p += 1

# 결과 출력
print(n, p)
