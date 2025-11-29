import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

# 세트 할인 전 총 가격
total = sum(burgers) + sum(sides) + sum(drinks)

# 비싼 것부터 세트로 묶기 위해 내림차순 정렬
burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

# 만들 수 있는 세트 수
S = min(B, C, D)

# 세트로 묶인 것들의 할인액 계산 (각 세트의 합의 10% 할인)
discount = 0
for i in range(S):
    discount += (burgers[i] + sides[i] + drinks[i]) // 10

print(total)
print(total - discount)
