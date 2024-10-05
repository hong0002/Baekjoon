# 입력 받기
a, b, x, y = map(int, input().split())

# 직접 이동 거리 계산
direct_distance = abs(a - b)

# 텔레포터를 사용하는 두 가지 방법 중 작은 값 계산
teleport_distance1 = abs(a - x) + abs(y - b)
teleport_distance2 = abs(a - y) + abs(x - b)

# 최소 거리 계산
min_distance = min(direct_distance, teleport_distance1, teleport_distance2)

# 결과 출력
print(min_distance)
