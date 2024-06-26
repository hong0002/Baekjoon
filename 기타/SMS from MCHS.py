# 입력을 받습니다.
t1, v1 = map(int, input().split())
t2, v2 = map(int, input().split())

# 조건을 체크하고 적절한 메시지를 출력합니다.
if t2 < 0 and v2 >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif t2 < t1:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif v2 > v1:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")
