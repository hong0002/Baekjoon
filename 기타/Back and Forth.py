import sys

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    s = sys.stdin.readline().rstrip('\n')
    if is_palindrome(s):
        print("beep")
    else:
        print("boop")

if __name__ == "__main__":
    main()
