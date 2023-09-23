n = input()
if n[-1] == '0':
    a = n[:len(n)-2]
    b = 10
else:
    a = n[:len(n)-1]
    b = n[-1]

print(int(a)+int(b))
