from collections import Counter

# 입력 받기
n = int(input())
draw_count = 10 * n
frequency = Counter()

# 각 추첨 번호의 빈도를 계산
for _ in range(draw_count):
    numbers = map(int, input().split())
    frequency.update(numbers)

# 기준치 이상으로 등장한 숫자 찾기
suspicious_numbers = [num for num, count in frequency.items() if count > 2 * n]

# 결과 출력
if suspicious_numbers:
    print(" ".join(map(str, sorted(suspicious_numbers))))
else:
    print(-1)
