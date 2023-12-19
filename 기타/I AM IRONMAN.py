import sys
input = sys.stdin.readline

n, p = map(int, input().split())
w, l, g = map(int, input().split())

win = set()
for _ in range(p):
    name, wl = input().split()
    if wl == 'W': win.add(name)

flag = False
score = 0
for _ in range(n):
    name = input().rstrip()

    if name in win:
        score += w
    else:
        score -= l
        if score < 0: score = 0

    if score >= g:
        flag = True
        break

print("I AM NOT IRONMAN!!") if flag else print("I AM IRONMAN!!")
