import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    while True:
        i = s.find("ABB")
        if i == -1:
            break
        # "ABB" -> "BA" (세 번째 문자는 삭제)
        s = s[:i] + "BA" + s[i+3:]

    print(s)
