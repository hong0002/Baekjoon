def is_lucky_lotto(s: str) -> bool:
    run = 1
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == 1:
            run += 1
            if run >= 5:
                return True
        else:
            run = 1
    return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    s = input().strip()
    print("YES" if is_lucky_lotto(s) else "NO")
