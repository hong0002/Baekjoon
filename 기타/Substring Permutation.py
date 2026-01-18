from collections import Counter

S = input().strip()
P = input().strip()

cntS = Counter(S)
cntP = Counter(P)

for c in cntP:
    if cntP[c] > cntS.get(c, 0):
        print("NO")
        break
else:
    print("YES")
