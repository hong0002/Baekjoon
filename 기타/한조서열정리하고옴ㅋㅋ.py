import sys

input = sys.stdin.readline
N = int(input().strip())
H = list(map(int, input().split()))

stack = []  # 인덱스 저장(높이 내림차순 유지)
ans = 0

for i, h in enumerate(H):
    # 현재가 더 크면, 스택에 있던 봉우리들의 "다음 더 큰 봉우리"는 현재 i
    while stack and H[stack[-1]] < h:
        j = stack.pop()
        ans = max(ans, i - j - 1)
    stack.append(i)

# 오른쪽에 더 큰 봉우리가 없는 경우 처리
while stack:
    j = stack.pop()
    ans = max(ans, N - j - 1)

print(ans)
