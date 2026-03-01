import sys

input = sys.stdin.readline

N = int(input())
students = []

for _ in range(N):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    # 국어 내림차순 -> -k
    # 영어 오름차순 -> e
    # 수학 내림차순 -> -m
    # 이름 오름차순 -> name
    students.append((name, -k, e, -m))

students.sort(key=lambda x: (x[1], x[2], x[3], x[0]))

out = []
for name, _, _, _ in students:
    out.append(name)

print("\n".join(out))
