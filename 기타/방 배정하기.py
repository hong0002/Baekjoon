a, b, c, n = map(int, input().split(" "))
rooms = [a, b, c]
flag = False

for first in range(n//a + 1):
    if flag: break
    for second in range(n//b + 1):
        if flag: break
        for third in range(n//c + 1):
            if flag: break
            if n - a*first - b*second - c*third == 0: flag = True

print(1) if flag else print(0)
