import sys
input = sys.stdin.read

data = input().strip().split()
index = 0
results = []

for _ in range(3):
    N = int(data[index])
    index += 1
    total = 0
    for _ in range(N):
        total += int(data[index])
        index += 1
    if total > 0:
        results.append('+')
    elif total < 0:
        results.append('-')
    else:
        results.append('0')

for result in results:
    print(result)
