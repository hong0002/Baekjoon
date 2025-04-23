def main():
    n = int(input())        # 문제 개수 입력
    excluded = 0            # 제외된 문제(홀수 난이도) 개수 카운터

    for _ in range(n):
        d = int(input())
        if d % 2 == 1:      # 홀수인지 검사
            excluded += 1

    print(excluded)

if __name__ == "__main__":
    main()
