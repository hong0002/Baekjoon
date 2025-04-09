# 입력 받기
C, K, P = map(int, input().split())

# 와인 총 개수를 저장하는 변수
total_wines = 0

# 1년 차부터 C년 차까지 와인 구매 수량 합산
for n in range(1, C+1):
    total_wines += K * n + P * n * n

# 결과 출력
print(total_wines)
