N = int(input().strip())

# F1=1, F2=1 로 두고 F_{N+1} 계산
a, b = 1, 1  # a=F1, b=F2
for _ in range(N-1):  # N=1이면 그대로 F2=1
    a, b = b, a + b   # 다음 항으로 이동

# N=1 -> b=1 = F2, N=2 -> b=2 = F3, ... 일반적으로 b가 F_{N+1}
print(b if N > 0 else 1)
