# 입력 받기
N = int(input())

# 자료형 판별
if -32768 <= N <= 32767:
    print("short")
elif -2147483648 <= N <= 2147483647:
    print("int")
else:
    print("long long")
