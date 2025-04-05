n = int(input())

if n == 0:
    print(1)
elif n > 0:
    # Python의 bit_length()는 양의 정수를 이진수로 표현했을 때 필요한 비트 수를 반환합니다.
    print(n.bit_length())
else:
    # 음수는 2의 보수 방식으로 32비트 전체가 저장됩니다.
    print(32)
