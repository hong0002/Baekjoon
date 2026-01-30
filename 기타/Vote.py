import sys

def parse_result_line(line: str):
    """
    한 줄: X (후보자명) + 공백 + R(정수) + 공백 + C(투표소)
    후보자명/투표소에 공백이 있을 수 있으므로,
    '처음 등장하는 숫자 토큰'을 R로 보고 그 앞을 X로 처리.
    """
    tokens = line.strip().split()
    idx = -1
    for i, t in enumerate(tokens):
        if t.isdigit():
            idx = i
            break
    # 문제 조건상 항상 존재
    x = " ".join(tokens[:idx])
    r = int(tokens[idx])
    # c = " ".join(tokens[idx+1:])  # 필요 없어서 미사용
    return x, r

def main():
    input = sys.stdin.readline
    P_line = input().strip()
    while P_line == "":
        P_line = input().strip()
    P = int(P_line)

    out = []
    for vote_idx in range(1, P + 1):
        # n, m 읽기 (빈 줄 방어)
        nm = input().strip()
        while nm == "":
            nm = input().strip()
        n_str, m_str = nm.split()
        n, m = int(n_str), int(m_str)

        candidates = []
        totals = {}

        for _ in range(n):
            name = input().rstrip("\n")
            # 혹시 공백 포함 이름이면 그대로 사용
            name = name.strip()
            candidates.append(name)
            totals[name] = 0

        for _ in range(m):
            line = input().rstrip("\n")
            line = line.strip()
            if not line:
                continue
            x, r = parse_result_line(line)
            # 후보자 목록에 있는 이름만 합산(문제상 항상 존재)
            if x in totals:
                totals[x] += r
            else:
                # 혹시 입력이 깔끔하지 않은 경우 대비: 후보명 trim 차이 등
                # 가장 단순하게는 그대로 추가(문제 조건이면 여기 오지 않음)
                totals[x] = totals.get(x, 0) + r

        max_score = max(totals.values()) if totals else 0
        winners = [name for name, score in totals.items() if score == max_score]

        if len(winners) == 1:
            w = winners[0]
            out.append(f"VOTE {vote_idx}: THE WINNER IS {w} {max_score}")
        else:
            out.append(f"VOTE {vote_idx}: THERE IS A DILEMMA")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
