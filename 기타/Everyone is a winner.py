# 입력 받기
M, K = map(int, input().split())

# 나누어 떨어지면 Yes, 그렇지 않으면 No
if M % K == 0:
    print("Yes")
else:
    print("No")
