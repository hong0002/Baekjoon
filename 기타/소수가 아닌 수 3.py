import sys

input = sys.stdin.readline

N = int(input().strip())
digits = list(map(int, input().split()))

nonprime_ones = {0, 1, 4, 6, 8, 9}

# 1) 소수가 아닌 한 자리수가 있으면 그거 출력
for d in digits:
    if d in nonprime_ones:
        print("YES")
        print(d)  # 한 자리 그대로
        sys.exit(0)

# 2) 전부 {2,3,5,7}인 경우: 같은 숫자 두 번 -> 11*a라 합성수
a = min(digits)
print("YES")
print(f"{a}{a}")
