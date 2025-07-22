import sys

def main():
    input = sys.stdin.readline

    # 1) 입력
    N = int(input().strip())
    char_delims = set(input().split())
    M = int(input().strip())
    digit_delims = set(input().split())
    K = int(input().strip())
    merges = set(input().split())
    S = int(input().strip())
    s = input().rstrip('\n')

    # 2) 효과적인 분리자 집합
    # 공백은 항상 분리자
    delims = (char_delims | digit_delims) - merges
    delims.add(' ')  # 스페이스도 분리자

    # 3) 문자열 순회하며 토큰화
    token = []
    for ch in s:
        if ch in delims:
            if token:
                print(''.join(token))
                token = []
        else:
            token.append(ch)

    # 4) 마지막 토큰 출력
    if token:
        print(''.join(token))

if __name__ == '__main__':
    main()
