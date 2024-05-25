def min_additional_sweets(A, B, C):
    max_val = max(A, B, C)
    additional_sweets = (max_val - A) + (max_val - B) + (max_val - C)
    return additional_sweets

# 입력값을 받습니다.
A, B, C = map(int, input().split())

# 결과를 출력합니다.
print(min_additional_sweets(A, B, C))
