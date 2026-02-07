import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        """return smallest idx such that prefix_sum(idx) >= k (1-indexed)"""
        idx = 0
        bitmask = 1 << (self.n.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1

def solve():
    n = int(input().strip())
    ks = [0] + list(map(int, input().split()))  # 1-indexed

    fw = Fenwick(n)
    for i in range(1, n + 1):
        fw.add(i, 1)

    alive = n
    cur_pos = 1
    cur_k = ks[cur_pos]

    while alive > 1:
        # cur_pos의 현재 alive-rank (1..alive)
        cur_rank = fw.sum(cur_pos)

        # 제거될 사람의 rank 계산
        offset = (cur_k - 1) % alive
        elim_rank = (cur_rank + offset - 1) % alive + 1

        elim_pos = fw.kth(elim_rank)
        fw.add(elim_pos, -1)
        alive -= 1

        if alive == 1:
            break

        # 제거된 사람의 다음 사람이 새 시작점
        next_rank = elim_rank
        if next_rank > alive:
            next_rank = 1
        cur_pos = fw.kth(next_rank)
        cur_k = ks[cur_pos]

    # 남은 1명
    ans = fw.kth(1)
    print(ans)

if __name__ == "__main__":
    solve()
