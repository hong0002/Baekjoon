# 역의 개수 N 입력
N = int(input())

# 각 역의 좌표 입력
stations = []
for _ in range(N):
    x, y = map(int, input().split())
    stations.append((x, y))

# 가장 남쪽에 있는 점 찾기
southmost_point = min(stations, key=lambda point: point[1])

# 결과 출력
print(f"{southmost_point[0]} {southmost_point[1]}")
