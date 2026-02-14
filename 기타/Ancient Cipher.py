import sys

enc = sys.stdin.readline().strip()
plain = sys.stdin.readline().strip()

def freq_sorted(s: str):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('A')] += 1
    freq.sort()
    return freq

print("YES" if freq_sorted(enc) == freq_sorted(plain) else "NO")
