# 입력 받기
N = int(input())
yesterday = input().strip()
today = input().strip()

# 어제와 오늘 모두 'C'인 공간 계산
count = 0
for i in range(N):
    if yesterday[i] == 'C' and today[i] == 'C':
        count += 1

# 결과 출력
print(count)
