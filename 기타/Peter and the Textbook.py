import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    alive = [True] * (n + 1)  # 1..n

    for _ in range(q):
        line = input().split()
        op = line[0]
        x = int(line[1])

        if op == '-':
            i = x
            j = n - i + 1
            alive[i] = False
            alive[j] = False
        elif op == '?':
            p = x
            cnt = 0
            for i in range(1, n + 1):
                if alive[i]:
                    cnt += 1
                    if cnt == p:
                        print(i)
                        break
