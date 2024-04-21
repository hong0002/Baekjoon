N = int(input())  # 임스가 계획하고 공부한 일수 입력 받기
planned_pages = list(map(int, input().split()))  # 임스가 공부하고자 계획한 페이지 수 입력 받기
actual_pages = list(map(int, input().split()))  # 임스가 공부한 페이지 수 입력 받기

# 임스가 계획한 페이지 수 이상으로 공부한 횟수를 저장할 변수 초기화
count = 0

# 각 날짜에 대해 비교하여 계획한 페이지 수 이상으로 공부한 경우 count를 증가시킴
for i in range(N):
    if actual_pages[i] >= planned_pages[i]:
        count += 1

# 결과 출력
print(count)
