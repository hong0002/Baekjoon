# 입력 받기
n = int(input())
words = input().split()

# 올바른 카운트 확인
is_valid = True
for i in range(n):
    # i+1이 올바른 숫자여야 함
    if words[i] != "mumble" and int(words[i]) != i + 1:
        is_valid = False
        break

# 결과 출력
if is_valid:
    print("makes sense")
else:
    print("something is fishy")
