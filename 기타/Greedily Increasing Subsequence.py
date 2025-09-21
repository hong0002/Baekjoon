import sys

data = sys.stdin.buffer.read().split()
N = int(data[0])
A = map(int, data[1:1+N])

ans = []
last = 0  # 원소가 1..N 이므로 0으로 시작해도 됨
for x in A:
    if x > last:
        ans.append(x)
        last = x

out = [str(len(ans)), "\n", " ".join(map(str, ans))]
sys.stdout.write("".join(out))
