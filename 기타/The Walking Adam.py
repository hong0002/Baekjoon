# 테스트 케이스의 개수 입력 받기
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # 각 테스트 케이스의 문자열 입력 받기
    steps = input()
    
    # 처음으로 'D'가 나오는 인덱스 찾기
    first_down_index = steps.find('D')
    
    # 만약 'D'가 없으면 전체 길이가 답
    if first_down_index == -1:
        print(len(steps))
    else:
        # 'D'가 나온 인덱스까지가 답
        print(first_down_index)
