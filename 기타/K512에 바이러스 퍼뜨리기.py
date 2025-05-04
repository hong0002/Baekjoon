import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    infected = [False] * (N + 1)
    cnt = 0  # 현재 감염된 컴퓨터 수

    out = []
    for _ in range(Q):
        q = input().split()
        t = int(q[0])
        if t == 1:
            x = int(q[1])
            if not infected[x]:
                infected[x] = True
                cnt += 1
        elif t == 2:
            x = int(q[1])
            if infected[x]:
                infected[x] = False
                cnt -= 1
        else:  # t == 3
            out.append(str(N - cnt))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
