# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    A, B = map(int, input().split(','))
    print(A + B)
