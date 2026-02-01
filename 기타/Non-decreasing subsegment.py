import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))

    best_len = 1
    best_sum = arr[0]

    cur_len = 1
    cur_sum = arr[0]

    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            cur_len += 1
            cur_sum += arr[i]
        else:
            # 새 구간 시작
            cur_len = 1
            cur_sum = arr[i]

        # 동점이면 "먼저 나온 것" 유지해야 하므로 '>' 일 때만 갱신
        if cur_len > best_len:
            best_len = cur_len
            best_sum = cur_sum

    print(best_len, best_sum)

if __name__ == "__main__":
    main()
