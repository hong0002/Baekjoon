S = input()

one_hole = set("abdegopqADOPQR@")
two_hole = set("B")

answer = 0

for ch in S:
    if ch in one_hole:
        answer += 1
    elif ch in two_hole:
        answer += 2

print(answer)
