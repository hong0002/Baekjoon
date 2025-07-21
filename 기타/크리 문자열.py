def longest_cri_substring_length(s: str) -> int:
    n = len(s)
    # 1) 숫자 배열과 prefix sum 생성
    d = [int(ch) for ch in s]
    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] + d[i]

    # 2) 짝수 길이 L를 큰 것부터 검사
    #    N이 짝수면 N, 홀수면 N-1부터 시작
    start_L = n if n % 2 == 0 else n - 1
    for L in range(start_L, 0, -2):
        half = L // 2
        for i in range(0, n - L + 1):
            sum_left  = P[i + half] - P[i]
            sum_right = P[i + L] - P[i + half]
            if sum_left == sum_right:
                return L
    # 문제 조건상 항상 존재하므로 여기에 도달하지 않음
    return 0

if __name__ == "__main__":
    import sys
    s = sys.stdin.readline().strip()
    print(longest_cri_substring_length(s))
