def max_satisfied_soldiers(N, A, B, C):
    return min(N, A) + min(N, B) + min(N, C)

# 입력
N = int(input())
A, B, C = map(int, input().split())

# 결과 출력
print(max_satisfied_soldiers(N, A, B, C))
