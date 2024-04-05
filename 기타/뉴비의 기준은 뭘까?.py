# 입력 받기
N, M = map(int, input().split())

# M이 뉴비, 올드비, TLE인지 판별하여 출력
if M <= 2:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")
