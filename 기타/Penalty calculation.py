# 입력 받기
n = int(input())  # 제출 횟수
submissions = []

# 제출 정보를 리스트로 저장
for _ in range(n):
    t, s = map(int, input().split())  # t: 제출 시간, s: 점수
    submissions.append((t, s))

# 최대 점수를 찾는다
max_score = max(s for _, s in submissions)

# 가장 높은 점수를 가진 가장 빨리 제출된 답안을 찾는다
for i, (t, s) in enumerate(submissions):
    if s == max_score:
        f = i + 1  # 답안 번호는 1부터 시작하므로 인덱스 + 1
        tf = t     # 해당 답안의 제출 시간
        sf = s     # 해당 답안의 점수
        break

# 페널티 계산
if sf == 0:
    penalty = 0
else:
    penalty = tf + (f - 1) * 20

# 결과 출력
print(penalty)
