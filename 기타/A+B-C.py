# 정수 A, B, C를 입력받음
A = int(input())
B = int(input())
C = int(input())

# 수로 생각할 때 A+B-C 계산
result_numeric = A + B - C

# 문자열로 생각할 때 A+B-C 계산
result_string = int(str(A) + str(B)) - C

# 결과 출력
print(result_numeric)
print(result_string)

