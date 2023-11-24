# 입력 받기
input_str = input().strip()

# 문자열을 공백을 기준으로 분리
a, operator, b, equal, c = input_str.split()

# 정수로 변환
a, b, c = int(a), int(b), int(c)

# 실제 합 계산
actual_sum = a + b

# 입력된 합과 실제 합을 비교하여 출력
if actual_sum == c:
    print("YES")
else:
    print("NO")
