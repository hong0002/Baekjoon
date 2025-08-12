import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    cnt = defaultdict(int)

    # 학생 선호도 입력 및 8가지 키에 대해 카운트 누적
    for _ in range(n):
        s, f, c = input().split()
        attrs = [s, f, c]
        for mask in range(8):  # 0~7
            key = []
            for i in range(3):  # 0:subject, 1:fruit, 2:color
                if mask & (1 << i):
                    key.append('-')
                else:
                    key.append(attrs[i])
            cnt[tuple(key)] += 1

    # 질의 처리
    out_lines = []
    for _ in range(m):
        qs, qf, qc = input().split()
        out_lines.append(str(cnt[(qs, qf, qc)]))

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
