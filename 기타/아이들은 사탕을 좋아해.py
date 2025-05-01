import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    
    # 각 종류에서 K개씩 나눠줄 수 있는 아이 수 합산
    max_children = sum(c // K for c in candies)
    print(max_children)
