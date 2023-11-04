# 현재 시각 입력 받기
current_time = list(map(int, input().split()))

# 요리하는 데 필요한 시간 입력 받기
cooking_time = int(input())

# 현재 시각을 초로 변환
current_seconds = current_time[0] * 3600 + current_time[1] * 60 + current_time[2]

# 오븐구이가 끝나는 시각을 계산
end_time_seconds = (current_seconds + cooking_time) % (24 * 3600)

# 계산된 종료 시각을 시, 분, 초로 변환
end_time_hours = end_time_seconds // 3600
end_time_seconds %= 3600
end_time_minutes = end_time_seconds // 60
end_time_seconds %= 60

# 결과 출력
print(end_time_hours, end_time_minutes, end_time_seconds)
