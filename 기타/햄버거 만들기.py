a, b = map(int, input().split())
count = 0
while True:
    a -= 2
    b -= 1
    if a < 0 or b < 0: break
    count += 1

print(count)
