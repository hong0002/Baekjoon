import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    accepted = [[] for _ in range(N + 1)]
    cnt = [0] * (N + 1)

    while True:
        line = input().split()
        if not line:
            break
        c = int(line[0])
        if c == 0:
            break
        name = line[1]

        if cnt[c] < M:
            accepted[c].append(name)
            cnt[c] += 1

    # 학급별 정렬: 이름 길이 -> 사전순
    for c in range(1, N + 1):
        accepted[c].sort(key=lambda s: (len(s), s))

    out = []
    # 청팀(홀수) 먼저
    for c in range(1, N + 1, 2):
        for name in accepted[c]:
            out.append(f"{c} {name}")
    # 백팀(짝수) 다음
    for c in range(2, N + 1, 2):
        for name in accepted[c]:
            out.append(f"{c} {name}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
