import sys

s = sys.stdin.readline().strip()
n = len(s)
i = 0
out = []

while i < n:
    if i + 2 < n:
        a, b, c = s[i], s[i+1], s[i+2]
        # 세 글자가 서로 다르고, 집합이 {R,B,L}이면 콤보
        if a != b and b != c and a != c and {a, b, c} == {'R', 'B', 'L'}:
            out.append('C')
            i += 3
            continue
    # 단일 대응
    ch = s[i]
    if ch == 'R':
        out.append('S')
    elif ch == 'B':
        out.append('K')
    else:  # 'L'
        out.append('H')
    i += 1

print(''.join(out))
