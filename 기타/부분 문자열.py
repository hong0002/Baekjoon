import sys

def is_subsequence(s: str, t: str) -> bool:
    i = 0
    n = len(s)
    if n == 0:
        return True
    for ch in t:
        if i < n and ch == s[i]:
            i += 1
            if i == n:
                return True
    return i == n

out = []
for line in sys.stdin.buffer:
    line = line.decode().rstrip("\n")
    if not line:
        continue
    s, t = line.split()  # 문제에서 공백으로 구분, s/t에 공백 없음
    out.append("Yes" if is_subsequence(s, t) else "No")

sys.stdout.write("\n".join(out))
