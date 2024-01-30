# 초를 분과 초로 변환하는 함수 정의
def convert_to_minutes_and_seconds(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

# 입력 받기
times = [int(input()) for _ in range(4)]

# 총 이동 시간 계산
total_seconds = sum(times)
# 분과 초로 변환
total_minutes, remaining_seconds = convert_to_minutes_and_seconds(total_seconds)

# 결과 출력
print(total_minutes)
print(remaining_seconds)
