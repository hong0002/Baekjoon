a, b = map(int, input().split())
count = 1
for i in range(b):
    count += (a-1)+(a-2)*i
print(count)
