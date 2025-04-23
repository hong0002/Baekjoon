import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    # 회전별 (분자, 분모)의 쌍을 미리 정의
    pairs = [
        (A, C, B, D),  # k=0
        (C, D, A, B),  # k=1
        (D, B, C, A),  # k=2
        (B, A, D, C),  # k=3
    ]

    best_k = 0
    best_val = -1.0

    for k, (n1, d1, n2, d2) in enumerate(pairs):
        val = n1 / d1 + n2 / d2
        # 최댓값 갱신 시, k가 더 작으면 자동으로 선택됨
        if val > best_val:
            best_val = val
            best_k = k

    print(best_k)

if __name__ == "__main__":
    main()
