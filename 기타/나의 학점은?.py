import sys

# 입력 읽기
scores = list(map(int, sys.stdin.readline().split()))
hong_score = int(sys.stdin.readline())

# 내림차순으로 정렬된 scores에서 홍익이 점수의 등수(ranking)를 구한다.
# 리스트 인덱스는 0부터 시작하므로 +1 해준다.
rank = scores.index(hong_score) + 1

# 등수에 따라 학점을 매핑
if 1 <= rank <= 5:
    grade = "A+"
elif 6 <= rank <= 15:
    grade = "A0"
elif 16 <= rank <= 30:
    grade = "B+"
elif 31 <= rank <= 35:
    grade = "B0"
elif 36 <= rank <= 45:
    grade = "C+"
elif 46 <= rank <= 48:
    grade = "C0"
else:  # 49, 50 등
    grade = "F"

print(grade)
