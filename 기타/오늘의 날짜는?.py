from datetime import datetime, timedelta

# 현재 시간을 가져옴
local_time = datetime.now()

# 서울의 시차를 계산하여 UTC+0으로 변환
utc_time = local_time - timedelta(hours=9)  # 서울은 UTC+9

# 연도, 월, 일을 출력
print(utc_time.strftime("%Y"))
print(utc_time.strftime("%m"))
print(utc_time.strftime("%d"))
