# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 초기값 설정
max_length = 1
current_length = 1

# 배열 순회하며 증가 부분 리스트 계산
for i in range(1, n):
    if arr[i] > arr[i - 1]:  # 증가 조건
        current_length += 1
    else:  # 증가가 끊긴 경우
        max_length = max(max_length, current_length)
        current_length = 1

# 마지막 증가 리스트 길이 갱신
max_length = max(max_length, current_length)

# 결과 출력
print(max_length)
