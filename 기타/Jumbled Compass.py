# 입력 받기
n1 = int(input())  # 현재 방향
n2 = int(input())  # 목표 방향

# 시계 방향 회전 계산
clockwise = (n2 - n1 + 360) % 360
# 반시계 방향 회전 계산
counter_clockwise = (n1 - n2 + 360) % 360

# 최소 회전 값 출력
if clockwise <= counter_clockwise:
    # 시계 방향이 더 작거나 같으면 시계 방향으로
    print(clockwise)
else:
    # 반시계 방향이 더 작으면 반시계 방향으로
    print(-counter_clockwise)
