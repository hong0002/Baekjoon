# 피보나치 비스무리한 수열은 f(n) = f(n-1) + f(n-3)인 수열이다. f(1) = f(2) = f(3) = 1이며 피보나치 비스무리한 수열을 나열하면 다음과 같다.
#
# 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ...
#
# 자연수 n을 입력받아 n번째 피보나치 비스무리한 수열을 구해보자!
#
#
# 자연수 n(1 ≤ n ≤ 116)이 주어진다.
#
#
# n번째 피보나치 비스무리한 수를 출력한다.

def simi_fibo(num):
    arr = [0] * num
    arr[0] = 1
    arr[1] = 1
    arr[2] = 1
    for i in range(3, num):
        arr[i] = arr[i-1] + arr[i-3]

    return arr

n = int(input())
print(1) if n <= 3 else print(simi_fibo(n)[n-1])
