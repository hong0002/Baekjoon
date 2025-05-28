# 입력
A, B = map(int, input().split())

# turn = 0 이면 용태 차례, 1 이면 유진 차례
turn = 0
a, b = A, B

while True:
    if turn == 0:
        # 용태가 공격
        b += a
        if b >= 5:
            print("yt")   # 용태 승리
            break
    else:
        # 유진이 공격
        a += b
        if a >= 5:
            print("yj")   # 유진 승리
            break
    turn ^= 1  # 턴 교대
