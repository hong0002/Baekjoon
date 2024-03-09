# 세 개의 양의 정수를 입력 받기
a, b, c = map(int, input().split())

# 조건에 따라 결과 출력
if a + b == c or a + c == b or b + c == a:
    print(1)
elif a * b == c or a * c == b or b * c == a:
    print(2)
else:
    print(3)
