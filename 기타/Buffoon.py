# 입력 받기
N = int(input().strip())
votes = [int(input().strip()) for _ in range(N)]

# Carlos의 득표수는 첫 번째 값
carlos_votes = votes[0]

# 최다 득표수 계산
max_votes = max(votes)

# 결과 출력: Carlos의 득표수가 최다 득표수와 같으면 "S", 아니면 "N"
if carlos_votes == max_votes:
    print("S")
else:
    print("N")
