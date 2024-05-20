# 각 역에서 내린 사람 수와 탄 사람 수를 입력 받습니다.
stations = []
for _ in range(4):
    out, in_ = map(int, input().split())
    stations.append((out, in_))

# 기차에 있는 사람 수와 최대 사람 수를 초기화합니다.
current_passengers = 0
max_passengers = 0

# 각 역을 순서대로 처리합니다.
for out, in_ in stations:
    # 현재 기차에 있는 사람 수를 갱신합니다.
    current_passengers -= out  # 내린 사람 수를 뺍니다.
    current_passengers += in_  # 탄 사람 수를 더합니다.
    
    # 최대 사람 수를 갱신합니다.
    if current_passengers > max_passengers:
        max_passengers = current_passengers

# 결과를 출력합니다.
print(max_passengers)
