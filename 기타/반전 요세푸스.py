# 요세푸스 문제는 다음과 같다.
#
#  
# $1$번 사람 오른쪽에는
# $2$번 사람이 앉아 있고,
# $2$번 사람 오른쪽에는
# $3$번 사람이 앉아 있고, 계속하여 같은 방식으로
# $N$명의 사람들이 원을 이루며 앉아 있다.
# $N$번 사람 오른쪽에는
# $1$번 사람이 앉아 있다. 이제
# $K$(
# $\leq N$)번 사람을 우선 제거하고, 이후 직전 제거된 사람의 오른쪽의
# $K$번째 사람을 계속 제거해 나간다. 모든 사람이 제거되었을 때, 제거된 사람의 순서는 어떻게 될까?
#
# 이 문제의 답을 (
# $\boldsymbol{N}$,
# $\boldsymbol{K}$)–요세푸스 순열이라고 하며, (
# $7$,
# $3$)–요세푸스 순열은
# $\left<3, 6, 2, 7, 5, 1, 4\right>$가 된다.
#
# 하지만 한 방향으로만 계속 돌아가는 건 너무 지루하다. 따라서 요세푸스 문제에 재미를 더하기 위해
# $M$명의 사람이 제거될 때마다 원을 돌리는 방향을 계속해서 바꾸려고 한다. 이렇게 정의된 새로운 문제의 답을 (
# $\boldsymbol{N}$,
# $\boldsymbol{K}$,
# $\boldsymbol{M}$)–반전 요세푸스 순열이라고 하며, (
# $7$,
# $3$,
# $4$)–반전 요세푸스 순열은
# $\left<3, 6, 2, 7, \mathbf{1}, \mathbf{5}, \mathbf{4}\right>$가 된다.
#
#  
# $N$,
# $K$,
# $M$이 주어질 때, (
# $N$,
# $K$,
# $M$)–반전 요세푸스 순열을 계산해 보자.
#
#
# 첫째 줄에 정수
# $N$,
# $K$,
# $M$이 주어진다. (
# $1 \leq N \leq 5\ 000$,
# $1 \leq K, M \leq N$)
#
#
# (
# $N$,
# $K$,
# $M$)–반전 요세푸스 순열을 이루는 수들을 한 줄에 하나씩 순서대로 출력한다.

from collections import deque

n, k, m = map(int, input().split())
josephus_arr = deque()
[josephus_arr.append(i) for i in range(1, n+1)]

count = 0
flag = True
while josephus_arr:
    if flag:
        for _ in range(k-1):
            temp = josephus_arr.popleft()
            josephus_arr.append(temp)
        print(josephus_arr.popleft())
        count += 1
    else:
        for _ in range(k-1):
            temp = josephus_arr.pop()
            josephus_arr.appendleft(temp)
        print(josephus_arr.pop())
        count += 1
    if count == m: # m번 제거했을 때 방향 전환
        if flag:
            flag = False
        else:
            flag = True
        count = 0
