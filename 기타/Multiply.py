def multiply_large_numbers(A, B):
    return str(int(A) * int(B))


# 입력 처리
N, M = map(int, input().split())
A = input().strip()
B = input().strip()

# 결과 출력
print(multiply_large_numbers(A, B))
