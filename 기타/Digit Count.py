# 입력 처리
start, end, digit = input().split()
start, end, digit = int(start), int(end), digit

# 숫자 등장 횟수 변수
count = 0

# 범위 내 각 숫자 확인
for num in range(start, end + 1):
    # 숫자를 문자열로 변환하고, 주어진 숫자가 몇 번 등장하는지 셈
    count += str(num).count(digit)

# 결과 출력
print(count)
