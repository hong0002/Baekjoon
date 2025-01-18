def solve():
    n = int(input())  # 입력을 받습니다
    positions = []  # 1이 있는 비트의 위치를 저장할 리스트
    
    position = 0  # 비트의 위치를 추적할 변수
    while n > 0:
        if n & 1:  # 가장 오른쪽 비트가 1인지 확인
            positions.append(position)
        n >>= 1  # n을 오른쪽으로 한 칸 시프트
        position += 1  # 비트 위치를 증가시킴
    
    print(" ".join(map(str, positions)))  # 결과를 출력 (공백으로 구분)
