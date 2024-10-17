import math

# 입력 받기
p, q, s = map(int, input().split())

# LCM 계산
lcm_pq = (p * q) // math.gcd(p, q)

# 동시에 깜빡이는 시간이 s 이내에 존재하는지 확인
if lcm_pq <= s:
    print("yes")
else:
    print("no")
