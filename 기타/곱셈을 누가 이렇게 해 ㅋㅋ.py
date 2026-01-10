import sys

def wrong_mul(a: int, b: int) -> int:
    sa = str(a)[::-1]  # 일의 자리부터
    sb = str(b)[::-1]

    la, lb = len(sa), len(sb)
    m = min(la, lb)

    parts = []
    for i in range(m):
        parts.append(str((ord(sa[i]) - 48) * (ord(sb[i]) - 48)))

    if la > lb:
        for i in range(m, la):
            parts.append(sa[i])          # 남는 자리는 긴 수의 숫자 그대로
    elif lb > la:
        for i in range(m, lb):
            parts.append(sb[i])

    # parts는 일의자리쪽부터 쌓였으니 뒤집어서 붙이면 최종 문자열
    res_str = ''.join(reversed(parts))
    return int(res_str)

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []
    for _ in range(t):
        a, b = map(int, input().split())
        out.append("1" if wrong_mul(a, b) == a * b else "0")
    print("\n".join(out))

if __name__ == "__main__":
    main()
