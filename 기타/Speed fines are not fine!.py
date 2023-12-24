# 입력 받기
speed_limit = int(input())
recorded_speed = int(input())

# 속도 범위에 따라 벌금 계산
if recorded_speed <= speed_limit:
    print("Congratulations, you are within the speed limit!")
elif recorded_speed <= speed_limit + 20:
    fine = 100
    print(f"You are speeding and your fine is ${fine}.")
elif recorded_speed <= speed_limit + 30:
    fine = 270
    print(f"You are speeding and your fine is ${fine}.")
else:
    fine = 500
    print(f"You are speeding and your fine is ${fine}.")
