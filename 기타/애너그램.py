import sys

def is_anagram(a: str, b: str) -> bool:
    # 1) 두 문자열을 정렬한 결과가 동일한지 비교
    return sorted(a) == sorted(b)

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        a, b = input().split()
        if is_anagram(a, b):
            print(f"{a} & {b} are anagrams.")
        else:
            print(f"{a} & {b} are NOT anagrams.")

if __name__ == "__main__":
    main()
