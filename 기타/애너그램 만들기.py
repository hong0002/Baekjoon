import sys
from collections import Counter

def min_deletions_to_anagram(s1: str, s2: str) -> int:
    # 각 문자열의 알파벳 빈도 계산
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    # 모든 알파벳에 대해 빈도 차이 합산
    deletions = 0
    for ch in (set(cnt1.keys()) | set(cnt2.keys())):
        deletions += abs(cnt1[ch] - cnt2[ch])
    return deletions

def main():
    data = sys.stdin.read().split()
    s1, s2 = data[0], data[1]
    print(min_deletions_to_anagram(s1, s2))

if __name__ == "__main__":
    main()
