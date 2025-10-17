import sys

data = sys.stdin.read().strip().split()
t = int(data[0])
nums = list(map(int, data[1:]))

out_lines = []
for i, k in enumerate(nums, start=1):
    total = k * (k + 1) * (k + 2) // 6  # 테트라헤드론 수
    out_lines.append(f"{i}: {k} {total}")

print("\n".join(out_lines))
