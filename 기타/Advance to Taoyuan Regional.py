from datetime import datetime, timedelta

# 입력 받은 날짜를 datetime 객체로 변환
input_date_str = input().strip()
input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

# ICPC Taoyuan Regional Contest 날짜
contest_date = datetime(2023, 10, 21)

# 35일 전 날짜 계산
deadline_date = contest_date - timedelta(days=35)

# 입력 날짜와 35일 전 날짜를 비교
if input_date > deadline_date:
    print("TOO LATE")
else:
    print("GOOD")
