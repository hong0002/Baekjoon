# 입력 받기
n = int(input())
containers = list(map(float, input().split()))

# 최대 크기의 하나의 큐브로 모든 BAPC 액체를 담을 수 있는 크기 계산
max_side_length = max(containers)
total_volume = sum([side**3 for side in containers])
required_side_length = round(total_volume**(1/3), 9)  # 반올림하여 소수점 아래 9자리까지 출력

print(required_side_length)
