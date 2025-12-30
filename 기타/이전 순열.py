import sys

def prev_permutation(a):
    n = len(a)

    # 1) i 찾기: a[i-1] > a[i] 되는 가장 오른쪽 i
    i = n - 1
    while i > 0 and a[i - 1] < a[i]:
        i -= 1

    # 전체가 오름차순이면 이전 순열 없음
    if i == 0:
        return None

    # 2) j 찾기: a[i-1] > a[j] 를 만족하는 가장 오른쪽 j
    j = n - 1
    while a[i - 1] < a[j]:
        j -= 1

    # 3) swap
    a[i - 1], a[j] = a[j], a[i - 1]

    # 4) i..끝 구간 뒤집기(내림차순 만들기)
    a[i:] = reversed(a[i:])
    return a

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))

    ans = prev_permutation(a)
    if ans is None:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
