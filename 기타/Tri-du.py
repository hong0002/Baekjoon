def max_probability_card(A, B):
    if A == B:
        return A
    else:
        return max(A, B)

# 입력 받기
A, B = map(int, input().split())

# 결과 출력
print(max_probability_card(A, B))
