import math

# 반지름 R을 입력받습니다.
R = int(input())

# 유클리드 기하학에서 원의 넓이
euclidean_area = math.pi * R * R

# 택시 기하학에서 원의 넓이
taxicab_area = 2 * R * R

# 결과를 출력합니다.
print(f"{euclidean_area:.6f}")
print(f"{taxicab_area:.6f}")
