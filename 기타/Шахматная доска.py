# 입력 받기
n = int(input())

# 체스판의 열과 행에 해당하는 값을 계산
row = (n - 1) // 8
col = (n - 1) % 8

# 열과 행에 해당하는 값을 문자로 변환
column_letter = chr(ord('a') + col)
row_number = row + 1

# 결과 출력
print(column_letter + str(row_number))
