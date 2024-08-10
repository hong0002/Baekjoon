def find_missing_number(numbers):
    # 숫자들을 정렬합니다.
    numbers.sort()
    
    # 첫 번째와 두 번째 숫자의 차이
    diff1 = numbers[1] - numbers[0]
    # 두 번째와 세 번째 숫자의 차이
    diff2 = numbers[2] - numbers[1]
    
    # 세 가지 경우를 고려합니다.
    if diff1 == diff2:
        # 등차수열이 이미 완성된 경우, 빠진 숫자는 마지막 숫자 뒤에 있는 것
        return numbers[2] + diff1
    elif diff1 < diff2:
        # 첫 번째와 두 번째 숫자 사이에 빠진 숫자가 있는 경우
        return numbers[1] + diff1
    else:
        # 두 번째와 세 번째 숫자 사이에 빠진 숫자가 있는 경우
        return numbers[0] + diff2

# 입력 받기
numbers = list(map(int, input().split()))

# 결과 출력
print(find_missing_number(numbers))
