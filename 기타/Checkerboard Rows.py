def solve():
    # 입력 받기
    num_boards = int(input())  # 체커보드의 개수
    
    for _ in range(num_boards):
        # 각 체커보드 정보 입력
        board_info = list(map(int, input().split()))
        
        k = board_info[0]  # 말의 개수
        pieces = board_info[1:]  # 말의 위치 (열, 행)
        
        # 8개의 행에 대해 말의 개수를 카운트
        row_count = [0] * 8  # 8개의 행에 대한 카운트를 저장
        
        for i in range(k):
            col = pieces[2*i]   # 열 (사용하지 않음)
            row = pieces[2*i + 1]  # 행
            row_count[row - 1] += 1  # 해당 행의 말 개수 증가 (행은 1부터 8까지)
        
        # 가장 많이 말이 놓인 행의 개수 찾기
        print(max(row_count))  # 최대값을 출력

# 함수 실행
solve()
