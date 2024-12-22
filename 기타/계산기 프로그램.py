# 첫 번째 숫자 입력 받기
result = int(input())

# 계속해서 연산자를 입력 받고 계산하기
while True:
    operator = input().strip()
    if operator == "=":
        print(result)  # 연산 결과 출력
        break
    number = int(input())
    
    if operator == "+":
        result += number
    elif operator == "-":
        result -= number
    elif operator == "*":
        result *= number
    elif operator == "/":
        result //= number  # 나눗셈은 소수점 버림 연산
