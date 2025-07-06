import sys
input = sys.stdin.readline

def main():
    N = int(input())
    # N까지의 숫자만 관심 있으므로, 문자열 길이로 걸러낼 기준
    maxlen = len(str(N))
    seen = bytearray(N+2)  # 0..N+1 까지 표시 가능

    for _ in range(N):
        s = input().strip()
        # 음수거나 길이가 너무 길면 무시
        if not s or s[0] == '-' or len(s) > maxlen:
            continue
        x = int(s)
        if 0 <= x <= N:
            seen[x] = 1

    # 0부터 순차적으로 빠진 첫 수를 찾음
    for i in range(N+2):
        if seen[i] == 0:
            print(i)
            return

if __name__ == "__main__":
    main()
