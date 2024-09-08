# t1과 t2 입력 받기
t1 = int(input())
t2 = int(input())

# 시퀀스 초기화
sequence = [t1, t2]

# 시퀀스를 구성하는 반복문
while sequence[-2] >= sequence[-1]:
    next_term = sequence[-2] - sequence[-1]
    sequence.append(next_term)

# 시퀀스의 길이 출력
print(len(sequence))
