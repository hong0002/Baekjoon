import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    pairs = []

    # a < b 이고 a + b = n
    # a < n - a  →  a < n/2
    for a in range(1, n):
        b = n - a
        if a < b:  # a != b 를 포함하는 조건
            pairs.append(f"{a} {b}")

    # 출력 형식 맞추기
    if pairs:
        print(f"Pairs for {n}: " + ", ".join(pairs))
    else:
        print(f"Pairs for {n}:")
