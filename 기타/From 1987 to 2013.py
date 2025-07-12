def next_distinct_year(Y):
    while True:
        Y += 1
        s = str(Y)
        # 모든 자리의 숫자가 중복되지 않는지 검사
        if len(set(s)) == len(s):
            return Y

if __name__ == "__main__":
    Y = int(input().strip())
    print(next_distinct_year(Y))
