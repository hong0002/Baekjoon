# 입력 받기
N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

# 총 거리 계산
total_distance = 0
for i in range(1, N):
    x1, y1 = coordinates[i - 1]
    x2, y2 = coordinates[i]
    total_distance += abs(x1 - x2) + abs(y1 - y2)

# 결과 출력
print(total_distance)
