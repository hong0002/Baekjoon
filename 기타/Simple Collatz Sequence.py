# 입력 받기
n = int(input())

# 단계 수를 저장할 변수 초기화
steps = 0

# n이 1이 될 때까지 반복
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n + 1
    steps += 1

# 결과 출력
print(steps)
