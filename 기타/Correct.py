# 입력값을 HH와 MM으로 분리
HH, MM = map(int, input().split())

# 대회가 시작한 시간 (9:00 AM)
start_time = 9 * 60

# 문제를 풀었을 때의 시간을 분으로 변환
solved_time = HH * 60 + MM

# 소요된 시간 계산 (시작 시간으로부터 문제를 풀 때까지의 시간)
time_consumed = solved_time - start_time

# 0 미만의 값은 0으로 설정 (대회 시작 전에 푼 경우)
if time_consumed < 0:
    time_consumed = 0

# 출력
print(time_consumed)
