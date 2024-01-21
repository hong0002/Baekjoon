# 입력값 받아오기
w = int(input())
l = int(input())
h = int(input())

# 조건 검사
min_dimension = min(w, l)
max_dimension = max(w, l)

# 조건에 따라 출력
if min_dimension / h >= 2 and max_dimension / min_dimension <= 2:
    print("good")
else:
    print("bad")
