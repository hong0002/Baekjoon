code = input()[:5]
n = int(input())
result = 0
for _ in range(n):
    new_subject = input()[:5]
    if code == new_subject: result += 1

print(result)
