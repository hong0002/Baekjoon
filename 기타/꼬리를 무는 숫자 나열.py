def manhattan_distance(num1, num2):
    def get_position(num):
        row = (num - 1) // 4
        col = (num - 1) % 4
        return row, col

    row1, col1 = get_position(num1)
    row2, col2 = get_position(num2)
    
    return abs(row1 - row2) + abs(col1 - col2)

# 입력받기
num1, num2 = map(int, input().split())

# 직각거리 계산
distance = manhattan_distance(num1, num2)

# 결과 출력
print(distance)
