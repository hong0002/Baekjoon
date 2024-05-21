# 입력을 받습니다.
X, L, R = map(int, input().split())

# 만약 X가 L과 R 사이에 있다면 X를 출력합니다.
if L <= X <= R:
    print(X)
else:
    # 그렇지 않다면 L과 R 중 X와 더 가까운 값을 출력합니다.
    if abs(X - L) < abs(X - R):
        print(L)
    else:
        print(R)
