photo = [input().split() for _ in range(15)]
flag1 = False
flag2 = False
flag3 = False
for i in photo:
    for j in i:
        if j == 'w': flag1 = True
        elif j == 'b': flag2 = True
        elif j == 'g': flag3 = True

if flag1: print("chunbae")
elif flag2: print("nabi")
elif flag3: print("yeongcheol")
