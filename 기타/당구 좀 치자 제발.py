# 입력 받기
N = int(input())  # N일
weather = list(map(int, input().split()))  # 날씨 정보 (0과 1로 이루어진 리스트)

# 초기 분노
anger = 0
total_anger = 0

# 날씨에 따라 분노 계산
for i in range(N):
    if weather[i] == 1:
        anger += 1  # 비가 오는 날에는 분노가 1 증가
    else:
        anger -= 1  # 비가 오지 않는 날에는 분노가 1 감소
    
    total_anger += anger  # 현재 분노를 총 분노에 더함

# 결과 출력
print(total_anger)
