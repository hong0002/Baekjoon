import sys
input = sys.stdin.readline

def main():
    msg = input().rstrip()   # "swi's cake is missing!"
    N = int(input().strip())

    S_list = []
    B_list = []
    for _ in range(N):
        M = int(input().strip())
        S = set(map(int, input().split()))
        B = int(input().strip())
        S_list.append(S)
        B_list.append(B)

    possible = []

    for x in range(1, N+1):  # x를 범인으로 가정
        ok = True
        for i in range(1, N+1):
            S = S_list[i-1]
            B = B_list[i-1]

            # 진술 내용이 참인지 계산
            if B == 1:
                content_true = (x in S)
            else:  # B == 0
                content_true = (x not in S)

            if i == x:
                # 범인은 거짓말해야 함
                if content_true:
                    ok = False
                    break
            else:
                # 나머지는 참말해야 함
                if not content_true:
                    ok = False
                    break

        if ok:
            possible.append(x)

    if not possible:
        print("swi")
    else:
        print(*possible)

if __name__ == "__main__":
    main()
