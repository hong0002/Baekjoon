def min_difference(a, b):
    # 세로로 자르는 경우
    vertical_cut1 = (a // 2) * b
    vertical_cut2 = (a - a // 2) * b
    vertical_diff = abs(vertical_cut1 - vertical_cut2)
    
    # 가로로 자르는 경우
    horizontal_cut1 = a * (b // 2)
    horizontal_cut2 = a * (b - b // 2)
    horizontal_diff = abs(horizontal_cut1 - horizontal_cut2)
    
    # 두 경우 중 최소 차이를 반환
    return min(vertical_diff, horizontal_diff)

# 입력
a, b = map(int, input().split())

# 결과 출력
print(min_difference(a, b))
