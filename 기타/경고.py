def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

# 입력 받기
current_time = input().strip()
throw_time = input().strip()

# 시간, 분, 초로 분리
current_hours, current_minutes, current_seconds = map(int, current_time.split(':'))
throw_hours, throw_minutes, throw_seconds = map(int, throw_time.split(':'))

# 초로 변환
current_seconds = time_to_seconds(current_hours, current_minutes, current_seconds)
throw_seconds = time_to_seconds(throw_hours, throw_minutes, throw_seconds)

# 시간 차이 계산
if throw_seconds <= current_seconds:
    throw_seconds += 24 * 3600  # 다음 날로 가정

wait_seconds = throw_seconds - current_seconds

# 최소 1초 기다리기
if wait_seconds == 0:
    wait_seconds = 1

# 결과 출력
print(seconds_to_time(wait_seconds))
