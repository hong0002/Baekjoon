# 입력 받기
n, k, T = map(int, input().split())
d = list(map(int, input().split()))

# 불쾌함 지수 초기화
discomfort_index = 0

# 온도 변화 시뮬레이션
for i in range(n):
    if T > k:
        T = T + d[i] - abs(T - k)
    elif T < k:
        T = T + d[i] + abs(T - k)
    else:
        T = T + d[i]
    
    # 불쾌함 지수 계산
    discomfort_index += abs(T - k)

# 결과 출력
print(discomfort_index)
