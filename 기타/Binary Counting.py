n, k = map(int, input().split())

sequence = ""

num = 0
# 충분히 길게 만들기 (넉넉하게)
while len(sequence) < 1000:
    sequence += bin(num)[2:]
    num += 1

result = []
idx = k - 1

for _ in range(5):
    result.append(sequence[idx])
    idx += n

print(" ".join(result))
