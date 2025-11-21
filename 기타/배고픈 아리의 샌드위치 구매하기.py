import sys

S, M = map(int, sys.stdin.readline().split())

# 아리 혼자 살 수 있는 경우
if S <= 1023:
    print("No thanks")
else:
    # 아리가 1023원을 모두 쓰고 나서 필요한 추가 금액
    D = S - 1023

    # 쿠기 돈 총합으로도 모자람
    if D > M:
        print("Impossible")
    # 쿠기 동전 부분집합으로 D를 정확히 만들 수 있는지 확인
    elif (D & M) == D:
        print("Thanks")
    else:
        print("Impossible")
