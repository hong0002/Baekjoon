# 입력 받기
n1, n2, n12 = map(int, input().split())

# Chapman 추정기를 사용하여 총 쥐 수 계산
N = ((n1 + 1) * (n2 + 1) // (n12 + 1)) - 1

# 결과 출력
print(N)
