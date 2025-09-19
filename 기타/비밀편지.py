# 입력
n = int(input().strip())
s = input().strip()

codes = {
    'A': '000000',
    'B': '001111',
    'C': '010011',
    'D': '011100',
    'E': '100110',
    'F': '101001',
    'G': '110101',
    'H': '111010',
}

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

ans = []
for i in range(n):
    chunk = s[6*i:6*(i+1)]
    decided = None
    for ch, pat in codes.items():
        if hamming(chunk, pat) <= 1:
            decided = ch
            break
    if decided is None:
        print(i + 1)  # 처음 모르는 문자 위치(1-based)
        exit(0)
    ans.append(decided)

print(''.join(ans))
