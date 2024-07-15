# 입력을 받습니다.
l, r = map(int, input().split())

# 조건에 따라 무스의 포인트를 계산합니다.
if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l + r}")
else:
    print(f"Odd {2 * max(l, r)}")
