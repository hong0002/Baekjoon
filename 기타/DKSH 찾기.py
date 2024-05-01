# 문자열 입력
s = input()

# DKSH가 몇 번 나타나는지 카운트
count = 0
for i in range(len(s) - 3):  # 문자열의 끝에서 DKSH의 길이를 뺀 만큼만 반복
    if s[i:i+4] == "DKSH":   # 현재 위치부터 4글자를 취하여 DKSH와 일치하는지 확인
        count += 1

print(count)
