s = input()
f1, f2, f3, f4, f5 = False, False, False, False, False
if 'M' in s:
    f1 = True
if 'O' in s:
    f2 = True
if 'B' in s:
    f3 = True
if 'I' in s:
    f4 = True
if 'S' in s:
    f5 = True

if f1 and f2 and f3 and f4 and f5:
    print("YES")
else:
    print("NO")
