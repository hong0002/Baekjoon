import sys
from collections import Counter

def classify(cards):
    cnt = Counter(cards)
    pattern = sorted(cnt.values(), reverse=True)

    if pattern == [1,1,1,1,1,1]:
        return "single"
    if pattern == [2,1,1,1,1]:
        return "one pair"
    if pattern == [2,2,1,1]:
        return "two pairs"
    if pattern == [2,2,2]:
        return "three pairs"
    if pattern == [3,1,1,1]:
        return "one triple"
    if pattern == [3,3]:
        return "two triples"
    if pattern == [4,1,1]:
        return "tiki"
    if pattern == [4,2]:
        return "tiki pair"
    if pattern == [3,2,1]:
        return "full house"

    # 문제 조건상 여기로 올 일 없음 (최대 4장 동일)
    return "single"

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        cards = list(map(int, input().split()))
        print(classify(cards))

if __name__ == "__main__":
    main()
