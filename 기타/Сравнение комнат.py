# 입력 받기
a, b, c, d = map(int, input().split())

# Машина и Петина комнаты의 넓이 계산
masha_area = a * b
petya_area = c * d

# 결과 출력
if masha_area > petya_area:
    print("M")
elif masha_area < petya_area:
    print("P")
else:
    print("E")
