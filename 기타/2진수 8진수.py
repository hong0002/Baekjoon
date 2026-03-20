s = input().strip()

# 길이가 3의 배수가 되도록 앞에 0을 붙임
while len(s) % 3 != 0:
    s = '0' + s

result = []

for i in range(0, len(s), 3):
    three = s[i:i+3]
    result.append(str(int(three, 2)))

print(''.join(result))
