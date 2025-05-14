# 입력
A, B = map(int, input().split())
C, D = map(int, input().split())

# 첫 번째, 두 번째 합
S1 = A + B
S2 = C + D

# 함수를 정의해 두 번 호출
def who(start, s):
    # start: 주사위를 굴린 사람 번호(1~4)
    # s: 굴린 주사위 눈의 합
    return 1 + ((start - 1) + (s - 1)) % 4

# 가동 계산 (첫 번째 롤러는 항상 1번)
G = who(1, S1)

# 진동 계산
J = who(G, S2)

print(J)
