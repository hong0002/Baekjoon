def middle(a, b, c):
    # 주어진 세 수를 리스트에 저장
    numbers = [a, b, c]
    
    # 리스트에서 최솟값과 최댓값을 찾아서 제외한 나머지 값을 반환
    result = [num for num in numbers if num != min(numbers) and num != max(numbers)]
    
    # 결과 출력
    print(result[0])

# 입력 받기
a, b, c = map(int, input().split())

# 함수 호출
middle(a, b, c)
