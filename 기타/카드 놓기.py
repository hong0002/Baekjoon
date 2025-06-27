import sys
from itertools import permutations

def main():
    input = sys.stdin.readline
    n = int(input())
    k = int(input())
    # 카드 숫자를 문자열로 읽어두면, 나중에 join할 때 편하다.
    cards = [input().strip() for _ in range(n)]
    
    results = set()
    # 모든 k장 순열에 대해 이어붙인 문자열을 집합에 추가
    for perm in permutations(cards, k):
        results.add(''.join(perm))
    
    # 서로 다른 문자열 개수 출력
    print(len(results))

if __name__ == "__main__":
    main()
