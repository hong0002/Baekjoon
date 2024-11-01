# 입력 받기
n = int(input())
distances = list(map(int, input().split()))

# 각 사람의 위치를 저장하기 위해 [(거리, 인덱스)] 형태로 생성
people = [(distances[i], i + 2) for i in range(n - 1)]

# 거리를 기준으로 정렬하여 원래 순서를 찾음
people.sort()

# 최종 줄서기 결과에 Jimmy를 포함하여 사람들의 순서를 결정
result = [1] + [person[1] for person in people]

# 결과 출력
print(" ".join(map(str, result)))
