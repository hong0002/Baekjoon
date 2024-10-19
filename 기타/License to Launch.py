# 입력 받기
n = int(input())  # 날짜 수
junk = list(map(int, input().split()))  # 각 날짜의 우주 쓰레기 양

# 최소값의 인덱스 찾기
min_junk = min(junk)  # 최소 우주 쓰레기 양
day_to_launch = junk.index(min_junk)  # 최소값이 나타난 첫 번째 날의 인덱스 찾기

# 결과 출력
print(day_to_launch)
