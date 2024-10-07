# 입력: 도미노 세트의 크기 N
N = int(input())

# 전체 점수 합을 저장할 변수
total_spots = 0

# 모든 가능한 (a, b) 쌍에 대해 점수를 합산
for a in range(N + 1):
    for b in range(a, N + 1):  # a <= b를 만족하는 쌍만 고려
        total_spots += a + b

# 결과 출력
print(total_spots)
