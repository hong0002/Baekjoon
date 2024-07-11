# 입력을 받습니다.
A, B, C = map(int, input().split())

# 세 정수를 리스트에 넣고 정렬합니다.
numbers = [A, B, C]
numbers.sort()

# 두 번째로 큰 수를 출력합니다.
print(numbers[1])
