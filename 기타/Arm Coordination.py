# 입력 받기
x, y = map(int, input().split())
r = int(input())

# 정사각형의 네 꼭짓점 계산
bottom_left = (x - r, y - r)
top_left = (x - r, y + r)
top_right = (x + r, y + r)
bottom_right = (x + r, y - r)

# 결과 출력 (시계 방향)
print(bottom_left[0], bottom_left[1])
print(top_left[0], top_left[1])
print(top_right[0], top_right[1])
print(bottom_right[0], bottom_right[1])
