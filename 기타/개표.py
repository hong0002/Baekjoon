import sys

def main():
    data = sys.stdin.read().split()
    T = int(data[0])
    for i in range(T):
        n = int(data[1 + i])
        full = n // 5        # '++++ ' 묶음 개수
        rem  = n % 5         # 남은 '|' 개수

        # '++++ '을 full번, '|'을 rem번
        s = '++++ ' * full + '|' * rem
        # 맨 뒤에 공백이 남아있으면 제거
        s = s.rstrip()
        print(s)

if __name__ == '__main__':
    main()
