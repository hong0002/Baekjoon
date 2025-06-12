def compute_score():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    total = 0    # 최종 점수
    bonus = 0    # 현재 보너스 점수

    # i: 문제 번호 (1부터), ch: 'O' 또는 'X'
    for i, ch in enumerate(S, start=1):
        if ch == 'O':
            total += i + bonus
            bonus += 1
        else:
            bonus = 0

    print(total)

if __name__ == "__main__":
    compute_score()
