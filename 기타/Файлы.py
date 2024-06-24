# 입력 받기
n = int(input().strip())
file_names = [input().strip() for _ in range(n)]
m = int(input().strip())
intervals = [tuple(map(int, input().strip().split())) for _ in range(m)]

# 결과 리스트
result = []

# 각 구간에 해당하는 파일 이름을 결과 리스트에 추가
for l, r in intervals:
    result.extend(file_names[l-1:r])

# 결과 출력
for file_name in result:
    print(file_name)
