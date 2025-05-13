def is_true_purple(h_lo, h_hi, s_lo, s_hi, v_lo, v_hi, R, G, B):
    # 1) V, M, m 계산
    M = max(R, G, B)
    m = min(R, G, B)
    V = M

    # 2) S 계산 (V > 0인 것은 R,G,B가 서로 다르기 때문에 보장됨)
    S = 255 * (V - m) / V

    # 3) H 계산
    if V == R:
        H = 60 * (G - B) / (V - m)
    elif V == G:
        H = 120 + 60 * (B - R) / (V - m)
    else:  # V == B
        H = 240 + 60 * (R - G) / (V - m)

    # 4) H를 [0, 360) 범위로 조정
    if H < 0:
        H += 360

    # 5) 범위 검사 (모두 포함 검사)
    return (h_lo <= H <= h_hi) and (s_lo <= S <= s_hi) and (v_lo <= V <= v_hi)


def main():
    import sys
    input = sys.stdin.readline

    h_lo, h_hi = map(int, input().split())
    s_lo, s_hi = map(int, input().split())
    v_lo, v_hi = map(int, input().split())
    R, G, B    = map(int, input().split())

    if is_true_purple(h_lo, h_hi, s_lo, s_hi, v_lo, v_hi, R, G, B):
        print("Lumi will like it.")
    else:
        print("Lumi will not like it.")


if __name__ == "__main__":
    main()
