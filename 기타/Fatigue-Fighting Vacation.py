# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

D, C, R = map(int, data[:3])
tiring_activities = list(map(int, data[3:3+C]))
invigorating_activities = list(map(int, data[3+C:]))

# 초기 변수 설정
current_disposition = D
activity_count = 0
tiring_index = 0
invigorating_index = 0

# 활동 수행
while True:
    # 피로 활동 수행
    while tiring_index < C and current_disposition >= tiring_activities[tiring_index]:
        current_disposition -= tiring_activities[tiring_index]
        tiring_index += 1
        activity_count += 1

    # 회복 활동 수행
    if invigorating_index < R:
        current_disposition += invigorating_activities[invigorating_index]
        invigorating_index += 1
        activity_count += 1
    else:
        # 회복 활동도 없으면 종료
        break

# 결과 출력
print(activity_count)
