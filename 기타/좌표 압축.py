import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # 1) 서로 다른 값 정렬
    uniq = sorted(set(arr))

    # 2) 값 -> 압축값(순위) 매핑
    rank = {v: i for i, v in enumerate(uniq)}

    # 3) 원래 순서대로 출력
    out = ' '.join(str(rank[x]) for x in arr)
    sys.stdout.write(out)

if __name__ == "__main__":
    main()
