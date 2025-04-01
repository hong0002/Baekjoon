# 입력 받기
n = int(input())
posts = [tuple(map(int, input().split())) for _ in range(n)]

max_area_twice = 0

# 각 점을 오른쪽 각의 꼭짓점으로 가정
for i in range(n):
    x, y = posts[i]
    for j in range(n):
        if posts[j][0] == x:  # x좌표가 같은 점 (수직 변)
            for k in range(n):
                if posts[k][1] == y:  # y좌표가 같은 점 (수평 변)
                    # 넓이의 두 배 = 수직변 길이 * 수평변 길이
                    area_twice = abs(posts[j][1] - y) * abs(posts[k][0] - x)
                    max_area_twice = max(max_area_twice, area_twice)

print(max_area_twice)
