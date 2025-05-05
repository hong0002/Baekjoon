import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    T = int(input())                # 테스트 케이스 개수
    for _ in range(T):
        V = int(input())            # 쪽지 개수
        notes = [int(input()) for _ in range(V)]
        
        # 숫자의 빈도를 센다
        cnt = Counter(notes)
        # 최대 빈도값
        max_freq = max(cnt.values())
        # 최대 빈도값을 가진 숫자들 중에서 가장 작은 수를 고른다
        answer = min(num for num, freq in cnt.items() if freq == max_freq)
        
        print(answer)

if __name__ == "__main__":
    main()
