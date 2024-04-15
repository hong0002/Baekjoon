# 함수 정의: 방향 변경
def change_direction(current_direction, instruction):
    directions = ['N', 'E', 'S', 'W']  # 북, 동, 남, 서
    if instruction == 1:  # 우향우
        return directions[(directions.index(current_direction) + 1) % 4]
    elif instruction == 2:  # 뒤로 돌아
        return directions[(directions.index(current_direction) + 2) % 4]
    elif instruction == 3:  # 좌향좌
        return directions[(directions.index(current_direction) - 1) % 4]

# 초기 방향 설정
current_direction = 'N'

# 주어진 지시 수행
for _ in range(10):
    instruction = int(input())  # 각각의 지시를 입력으로 받음
    current_direction = change_direction(current_direction, instruction)

# 최종 방향 출력
print(current_direction)
