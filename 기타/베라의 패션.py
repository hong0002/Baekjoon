def color_combinations(N):
    if N == 1:
        return 0
    else:
        # 상의와 하의가 서로 다른 색상인 조합의 가짓수는 N * (N-1)
        return N * (N - 1)

# 입력 받기
N = int(input())

# 결과 출력
result = color_combinations(N)
print(result)
