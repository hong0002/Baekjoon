# 입력 받기
Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

# 베시의 거리 (Chebyshev Distance)
bessie_distance = max(abs(Br - Jr), abs(Bc - Jc))

# 데이지의 거리 (Manhattan Distance)
daisy_distance = abs(Dr - Jr) + abs(Dc - Jc)

# 결과 비교
if bessie_distance < daisy_distance:
    print("bessie")
elif daisy_distance < bessie_distance:
    print("daisy")
else:
    print("tie")
