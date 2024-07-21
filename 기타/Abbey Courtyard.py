import math

def calculate_wiring_length(area):
    # 한 변의 길이는 면적의 제곱근
    side_length = math.sqrt(area)
    
    # 전체 둘레는 한 변의 길이의 4배
    perimeter = 4 * side_length
    
    return perimeter

# 입력 받기
area = int(input())

# 전선 길이 계산
wiring_length = calculate_wiring_length(area)

# 출력
print(f"{wiring_length:.9f}")
