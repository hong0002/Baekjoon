def calculate_youngsik_cost(call_durations):
    total_cost = 0
    for duration in call_durations:
        total_cost += (duration // 30 + 1) * 10
    return total_cost

def calculate_minsik_cost(call_durations):
    total_cost = 0
    for duration in call_durations:
        total_cost += (duration // 60 + 1) * 15
    return total_cost

# 입력 받기
n = int(input())
call_durations = list(map(int, input().split()))

# 요금 계산
youngsik_cost = calculate_youngsik_cost(call_durations)
minsik_cost = calculate_minsik_cost(call_durations)

# 결과 출력
if youngsik_cost < minsik_cost:
    print(f"Y {youngsik_cost}")
elif minsik_cost < youngsik_cost:
    print(f"M {minsik_cost}")
else:
    print(f"Y M {youngsik_cost}")
