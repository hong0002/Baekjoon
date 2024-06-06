def calculate_time(M, S, G, A, B, L, R):
    # 왼쪽 줄 (걷기)의 소요 시간 계산
    time_walk_queue = L / A  # 모든 사람이 다 올라가는 데 걸리는 시간
    time_walk_escalator = M / G  # 파울리나가 올라가는 데 걸리는 시간
    total_time_walk = time_walk_queue + time_walk_escalator

    # 오른쪽 줄 (서기)의 소요 시간 계산
    time_stand_queue = R / B  # 모든 사람이 다 올라가는 데 걸리는 시간
    time_stand_escalator = M / S  # 파울리나가 올라가는 데 걸리는 시간
    total_time_stand = time_stand_queue + time_stand_escalator

    # 더 짧은 시간을 선택
    if total_time_walk < total_time_stand:
        return "friskus"
    else:
        return "latmask"

# 입력
M, S, G = map(int, input().strip().split())
A, B = map(float, input().strip().split())
L, R = map(int, input().strip().split())

# 결과 출력
print(calculate_time(M, S, G, A, B, L, R))
