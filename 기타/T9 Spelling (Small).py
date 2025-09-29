import sys

# 키패드 매핑
groups = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
    '0': " "
}

# 문자 -> (키, 횟수) 역매핑 만들기
char2press = {}
for key, letters in groups.items():
    for idx, ch in enumerate(letters):
        char2press[ch] = (key, idx + 1)

data = sys.stdin.read().splitlines()
t = int(data[0].strip())
lines = data[1:]

for case_idx in range(1, t + 1):
    s = lines[case_idx - 1].rstrip('\n')
    out = []
    last_key = None

    for ch in s:
        key, cnt = char2press[ch]
        if last_key == key:
            out.append(' ')  # 같은 키면 공백으로 pause
        out.append(key * cnt)
        last_key = key

    print(f"Case #{case_idx}: {''.join(out)}")
