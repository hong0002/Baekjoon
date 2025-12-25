import sys

def decrypt_line(s: str) -> str:
    res = []
    for ch in s:
        if 'A' <= ch <= 'Z':
            # A(0) -> V(21): (idx - 5) mod 26
            idx = ord(ch) - ord('A')
            res.append(chr((idx - 5) % 26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)

lines = [line.rstrip('\n') for line in sys.stdin]

i = 0
out = []
while i < len(lines):
    if lines[i] == "ENDOFINPUT":
        break
    if lines[i] == "START":
        cipher = lines[i + 1]
        out.append(decrypt_line(cipher))
        # lines[i+2] should be "END"
        i += 3
    else:
        # 문제 조건상 여기로 오면 안 되지만, 안전하게 스킵
        i += 1

print("\n".join(out))
