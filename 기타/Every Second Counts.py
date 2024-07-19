def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

# 입력을 받습니다.
start_time = input().strip()
end_time = input().strip()

# 시작 시간과 종료 시간을 각각 시, 분, 초로 나눕니다.
start_h, start_m, start_s = map(int, start_time.split(' : '))
end_h, end_m, end_s = map(int, end_time.split(' : '))

# 시작 시간과 종료 시간을 초 단위로 변환합니다.
start_seconds = time_to_seconds(start_h, start_m, start_s)
end_seconds = time_to_seconds(end_h, end_m, end_s)

# 만약 종료 시간이 시작 시간보다 작다면 24시간을 더합니다.
if end_seconds < start_seconds:
    end_seconds += 24 * 3600

# 두 시간의 차이를 계산합니다.
elapsed_seconds = end_seconds - start_seconds

# 결과를 출력합니다.
print(elapsed_seconds)
