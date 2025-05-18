import sys

def add_binary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += (a[i] == '1')
            i -= 1
        if j >= 0:
            total += (b[j] == '1')
            j -= 1
        res.append('1' if total % 2 else '0')
        carry = total // 2
    return ''.join(reversed(res))

def main():
    a, b = sys.stdin.readline().split()
    print(add_binary(a, b))

if __name__ == "__main__":
    main()
