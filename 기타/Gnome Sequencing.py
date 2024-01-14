def check_order(beards):
    if beards[0] < beards[1] < beards[2] or beards[0] > beards[1] > beards[2]:
        return "Ordered"
    else:
        return "Unordered"

# 입력 받기
N = int(input())
print("Gnomes:")

# 각 그룹에 대해 결과 출력
for _ in range(N):
    beard_lengths = list(map(int, input().split()))
    result = check_order(beard_lengths)
    print(result)
