n = int(input())
menu_cost = [int(input()) for _ in range(n)]
m = int(input())
result = 0
for _ in range(m):
    b = int(input())
    result += menu_cost[b-1]
print(result)
