# A와 B 입력 받기
A, B = map(int, input().split())

# 몫과 나머지 계산
quotient = A // B
remainder = A % B

# 나머지가 음수라면 몫을 하나 더 빼고 나머지를 보정
if remainder < 0:
    quotient += 1
    remainder -= B

# 출력
print(quotient)
print(remainder)
