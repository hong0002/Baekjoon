import sys

def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, m, k = map(int, line.split())
        if n == 0 and m == 0 and k == 0:
            break

        people = list(range(1, n + 1))
        idx = 0  # 다음 카운트를 시작할 위치(0-based)

        eliminated_count = 0
        while True:
            idx = (idx + m - 1) % len(people)  # m번째 사람 위치로 이동
            eliminated = people.pop(idx)        # 제거
            eliminated_count += 1

            if eliminated_count == k:
                out.append(str(eliminated))
                break
            # pop 후 idx는 자동으로 "제거된 사람의 다음 사람"을 가리키게 됨

    print("\n".join(out))

if __name__ == "__main__":
    solve()
