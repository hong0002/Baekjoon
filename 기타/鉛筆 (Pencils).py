def min_cost_to_buy_pencils(N, A, B, C, D):
    # 세트 X의 최소 비용 계산
    # N/A 값을 올림하여 필요한 세트 수를 구함
    sets_needed_X = (N + A - 1) // A
    cost_X = sets_needed_X * B
    
    # 세트 Y의 최소 비용 계산
    # N/C 값을 올림하여 필요한 세트 수를 구함
    sets_needed_Y = (N + C - 1) // C
    cost_Y = sets_needed_Y * D
    
    # 두 세트 비용 중 더 작은 값 선택
    return min(cost_X, cost_Y)

# 입력을 받습니다.
N, A, B, C, D = map(int, input().split())

# 최소 비용을 계산합니다.
result = min_cost_to_buy_pencils(N, A, B, C, D)

# 결과를 출력합니다.
print(result)
