# 입력받은 실수 x의 내림값을 구하는 코드

# 입력을 받고, 앞뒤 공백을 제거합니다.
x = input().strip()

# 문자열을 부동소수점 수로 변환합니다.
x = float(x)

# 양수의 경우 int()는 내림과 같은 역할을 합니다.
print(int(x))
