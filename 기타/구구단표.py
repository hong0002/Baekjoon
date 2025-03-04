n = int(input())
gugu = set()
for i in range(1, 10):
    for j in range(1, 10):
        gugu.add(i * j)
print(1) if n in gugu else print(0)
