import math

def extra_cutting_effort(w, h):
    diagonal_length = math.sqrt(w ** 2 + h ** 2)
    rectangle_cutting_effort = w + h
    diagonal_cutting_effort = diagonal_length
    return rectangle_cutting_effort - diagonal_cutting_effort

# 입력 받기
w, h = map(int, input().split())

# 결과 출력
print(extra_cutting_effort(w, h))

