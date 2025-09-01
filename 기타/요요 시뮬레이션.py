import sys

W0, I0, T = map(int, sys.stdin.readline().split())
D, I, A = map(int, sys.stdin.readline().split())

def simulate(change_bmr: bool):
    W = W0
    B = I0
    for _ in range(D):
        delta = I - (B + A)   # 하루 에너지 수지 (g)
        W += delta            # 1) 체중 변화
        if W <= 0:
            return None       # Danger Diet

        if change_bmr and abs(delta) > T:
            # 2) 기초대사량 변화 (체중 변화 후 적용)
            B += delta // 2   # 파이썬 // 는 음수도 바닥(내림)
            if B <= 0:
                return None   # Danger Diet
    return W, B

# 1) 기초 대사량 변화 미고려
res1 = simulate(change_bmr=False)
if res1 is None:
    print("Danger Diet")
else:
    W1, _ = res1
    print(W1, I0)

# 2) 기초 대사량 변화 고려 + 요요 판정
res2 = simulate(change_bmr=True)
if res2 is None:
    print("Danger Diet")
else:
    W2, B2 = res2
    yoyo = "YOYO" if I0 - (B2 + 0) > 0 else "NO"  # A0 = 0
    print(W2, B2, yoyo)
