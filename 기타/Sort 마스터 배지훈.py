# 입력 받기
N = int(input())  # 배열의 크기
A = list(map(int, input().split()))  # 배열 요소 입력 받기

# 배열 정렬
A.sort()

# 정렬된 배열의 마지막 원소 출력
print(A[-1])
