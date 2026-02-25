n = int(input())
days = set()

for _ in range(n):
    d = int(input())
    days.add(d)

print("YES" if len(days) < 5 else "NO")
