t = int(input())
scores = [0, 0, 0, 0 ,0]
for i, v in enumerate(map(int, input().split())):
    scores[i] = v

if scores[0] > scores[2]: sid = (scores[0] - scores[2]) * 508
else: sid = (scores[2] - scores[0]) * 108

if scores[1] > scores[3]: sid += (scores[1] - scores[3]) * 212
else: sid += (scores[3] - scores[1]) * 305

if scores[4] != 0: sid += scores[4] * 707

sid *= 4763
print(sid)
