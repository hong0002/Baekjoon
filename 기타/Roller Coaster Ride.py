N = int(input().strip())  # 내 위치
C = int(input().strip())  # 객차 수
P = int(input().strip())  # 한 객차당 인원

capacity = C * P  # 한 번에 태울 수 있는 총 인원

if N <= capacity:
    print("yes")
else:
    print("no")
