import sys

def next_valid_height(h0_str):
    # 문자열로 받은 h0를 8로 나눈 나머지를 구한다
    r = 0
    for ch in h0_str:
        r = (r*10 + (ord(ch)-48)) % 8

    # r==0 또는 r==5 이면 그대로, 아니면 보정
    if r == 0 or r == 5:
        return h0_str

    # 파이썬 big int 로 변환해도 되고, 문자열 덧셈으로 해도 되지만
    # 간단히 int 변환:
    h0 = int(h0_str)
    if r < 5:
        h = h0 + (5 - r)
    else:
        h = h0 + (8 - r)
    return str(h)

if __name__ == "__main__":
    h0 = sys.stdin.readline().strip()
    print(next_valid_height(h0))
