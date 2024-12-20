# Arno가 잠드는 시간과 알람 시간이 입력으로 주어집니다.
sleep_time = int(input())
wake_time = int(input())

# 잠드는 시간이 밤(20-23)이고, 알람 시간이 다음날 아침(5-10)일 경우 처리
if wake_time < sleep_time:
    sleep_duration = (24 - sleep_time) + wake_time
else:
    sleep_duration = wake_time - sleep_time

# 결과 출력
print(sleep_duration)
