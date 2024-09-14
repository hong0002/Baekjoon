# 입력 받기
n = int(input())  # 테스트 케이스의 수

for _ in range(n):
    # 두 숫자 입력 받기
    x, y = input().split()
    
    # 문자열로 된 숫자를 뒤집은 후, 정수로 변환하여 덧셈
    rev_x = int(x[::-1])
    rev_y = int(y[::-1])
    
    # 더한 결과를 다시 뒤집어서 출력
    result = str(rev_x + rev_y)[::-1]
    
    # 출력 시 선행 0 제거
    print(int(result))
