import sys

def ability_points(level: int) -> int:
    thresholds = [60, 100, 140, 200, 250]
    return sum(1 for t in thresholds if level >= t)

data = sys.stdin.read().strip().split()
N = int(data[0])
levels = list(map(int, data[1:]))

# 상위 42명(또는 N명) 선발
levels.sort(reverse=True)
picked = levels[:42]

level_sum = sum(picked)
ability_sum = sum(ability_points(lv) for lv in picked)

print(level_sum, ability_sum)
