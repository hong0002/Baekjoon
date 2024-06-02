def bee(A, B, C):
    total_bees = A + B + C
    target_bees_per_flower = total_bees // 3

    # 벌들의 이동 거리 계산
    moves_A_to_target = target_bees_per_flower - A
    moves_B_to_target = target_bees_per_flower - B
    moves_C_to_target = target_bees_per_flower - C

    # 이동 거리 계산
    total_moves = abs(moves_A_to_target) + abs(moves_C_to_target)
    return total_moves

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(bee(A, B, C))
