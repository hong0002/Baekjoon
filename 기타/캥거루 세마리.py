def max_jumps(A, B, C):
    # 각 캥거루 사이의 거리 계산
    distance1 = B - A
    distance2 = C - B
    
    # 최대 점프 수 계산
    max_jumps = max(distance1, distance2) - 1
    
    return max_jumps

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(max_jumps(A, B, C))
