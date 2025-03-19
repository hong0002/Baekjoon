import sys

def main():
    # sys.stdin을 통해 모든 입력을 읽어들임
    data = sys.stdin.read().strip().split()
    
    # 입력 데이터는 공백으로 분리된 문자열 리스트이므로, 두 개씩 순회합니다.
    i = 0
    while i < len(data):
        N = int(data[i])
        S = int(data[i+1])
        # 각 사람(및 판사)이 받을 주식의 최대 수는 S를 (N+1)로 나눈 몫입니다.
        print(S // (N + 1))
        i += 2

if __name__ == '__main__':
    main()
