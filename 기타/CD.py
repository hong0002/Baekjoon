import sys
input = sys.stdin.readline

def count_common(a, b):
    """두 정렬된 리스트 a, b에서 공통 원소의 개수를 두 포인터로 세기"""
    i = j = cnt = 0
    n, m = len(a), len(b)
    while i < n and j < m:
        if a[i] == b[j]:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return cnt

def main():
    out = []
    while True:
        line = input().split()
        if not line:
            break
        n, m = map(int, line)
        if n == 0 and m == 0:
            break

        # 상근이 CD 리스트
        a = [int(input()) for _ in range(n)]
        # 선영이 CD 리스트
        b = [int(input()) for _ in range(m)]

        # 두 포인터로 공통 개수 세기
        out.append(str(count_common(a, b)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
