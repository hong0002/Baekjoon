a = input()
b = input()

result = ""
for i in range(len(a)):
    result += max(a[i], b[i])

print(result)
