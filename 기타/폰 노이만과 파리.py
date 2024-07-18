# 입력을 받습니다.
S, T, D = map(int, input().split())

# 두 기차가 만날 때까지 걸리는 시간
time_to_meet = D / (2 * S)

# 파리가 이동한 거리
distance_flown = T * time_to_meet

# 결과를 출력합니다.
print(int(distance_flown))
