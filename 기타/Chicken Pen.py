import math

def draw_pen(N):
    # 1) 내부 크기 k, 전체 변 길이 s 계산
    k = math.ceil(N**0.5)
    s = k + 2

    # 2) 펜 테두리 문자열
    border = 'x' * s
    middle = 'x' + '.' * k + 'x'

    # 3) 출력
    print(border)
    for _ in range(k):
        print(middle)
    print(border)

if __name__ == '__main__':
    N = int(input().strip())
    draw_pen(N)
