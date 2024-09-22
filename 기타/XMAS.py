# 입력 받기
n = int(input())  # 손님의 수
picked = [0] * (n + 1)  # 각 손님이 가져간 선물 번호를 저장할 배열 (1-based index)

# 손님들이 가져간 선물 번호 입력 받기
for i in range(1, n + 1):
    picked[i] = int(input())

# 결과 저장할 리스트
result = [0] * (n + 1)

# 각 손님이 가져간 선물 번호를 바탕으로, 선물이 누구에게 갔는지 계산
for i in range(1, n + 1):
    recipient = picked[i]  # i번 손님이 가져간 선물 번호
    result[recipient] = i  # recipient는 i번 손님의 선물을 받음

# 결과 출력
for i in range(1, n + 1):
    print(result[i])
