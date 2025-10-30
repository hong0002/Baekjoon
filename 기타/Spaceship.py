import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

S = sum(arr)
half = S // 2  # 해가 존재하므로 정수임이 보장

# half와 같은 값을 가진 원소의 인덱스 하나를 찾는다.
last_idx = -1
for i, x in enumerate(arr):
    if x == half:
        last_idx = i
        break

# 출력: last_idx를 마지막으로, 나머지는 앞쪽에 (아무 순서나 OK)
res = [arr[i] for i in range(n) if i != last_idx] + [arr[last_idx]]
print(*res)
