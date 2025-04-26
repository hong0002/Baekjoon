# Python 3
A, a, B, b, P = map(int, input().split())

# 1) 판에 직접 배치
cond1 = (P >= A + B)
# 2) 큰 링 → 작은 링 스크랩
cond2 = (P >= B and b >= A)
# 3) 작은 링 → 큰 링 스크랩
cond3 = (P >= A and a >= B)

print("Yes" if (cond1 or cond2 or cond3) else "No")
