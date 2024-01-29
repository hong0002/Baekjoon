# 입력을 받습니다.
L = int(input())
messages = []
for _ in range(L):
    message = input().split()
    N = int(message[0])
    symbol = message[1]
    messages.append((N, symbol))

# 메시지를 디코딩하여 출력합니다.
for N, symbol in messages:
    print(symbol * N)
