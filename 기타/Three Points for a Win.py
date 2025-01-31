def calculate_total_points(N, A, B):
    total_points = 0
    for i in range(N):
        if A[i] > B[i]:
            total_points += 3  # Win
        elif A[i] == B[i]:
            total_points += 1  # Draw
    return total_points

# 입력 처리
N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(calculate_total_points(N, A, B))
