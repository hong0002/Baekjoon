def rev(n):
    # 정수를 문자열로 바꾼 후 역순으로 뒤집고, 다시 정수로 변환합니다.
    return int(str(n)[::-1])

# 입력 받기: 두 수를 공백으로 구분하여 입력받습니다.
x, y = map(int, input().split())

# Rev(Rev(X) + Rev(Y)) 계산 후 출력
print(rev(rev(x) + rev(y)))
