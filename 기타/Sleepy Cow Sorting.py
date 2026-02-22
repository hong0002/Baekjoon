import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    p = list(map(int, input().split()))
    
    # 뒤에서부터 "엄격히 증가"하는 suffix의 시작점을 찾는다
    idx = N - 1
    while idx > 0 and p[idx - 1] < p[idx]:
        idx -= 1
    
    # idx가 suffix 시작점이므로, 그 앞의 개수 = 최소 이동 횟수
    print(idx)

if __name__ == "__main__":
    main()
