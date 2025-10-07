import sys

def find(p, x):
    # 경로 압축
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(p, r, a, b):
    ra, rb = find(p, a), find(p, b)
    if ra == rb:
        return
    # 랭크/크기 대신 간단히 합치기 (n<=100이라 충분)
    if r[ra] < r[rb]:
        ra, rb = rb, ra
    p[rb] = ra
    if r[ra] == r[rb]:
        r[ra] += 1

def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    t = next(it, 0)
    out_lines = []
    for _ in range(t):
        n = next(it)
        k = next(it)
        parent = list(range(n))
        rank = [0]*n
        for _ in range(k):
            u = next(it); v = next(it)
            if 0 <= u < n and 0 <= v < n:
                union(parent, rank, u, v)
        # 연결 컴포넌트가 하나인지 확인
        if n == 0:
            out_lines.append("Connected.")  # 문제 조건상 n<=100, 0은 사실상 없음
        else:
            root0 = find(parent, 0)
            ok = all(find(parent, i) == root0 for i in range(n))
            out_lines.append("Connected." if ok else "Not connected.")
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
