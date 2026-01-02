import sys
from array import array

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    s = input().strip()

    rows = 5                 # vertex y: 0..4
    cols = 2 * N             # total cell-width
    V_total = (cols + 1) * rows

    # DSU: activate only when used (parent == -1 means inactive)
    parent = array('i', [-1]) * V_total
    size = array('I', [0]) * V_total

    # Edge existence to avoid duplicates
    # horizontal edge: between (x,y)-(x+1,y), x=0..cols-1, y=0..4
    h = bytearray(cols * rows)
    # vertical edge: between (x,y)-(x,y+1), x=0..cols, y=0..3
    v = bytearray((cols + 1) * (rows - 1))

    V = 0   # active vertices
    E = 0   # edges
    C = 0   # connected components among active vertices

    def vid(x, y):
        return x * rows + y

    def activate(i):
        nonlocal V, C
        if parent[i] == -1:
            parent[i] = i
            size[i] = 1
            V += 1
            C += 1

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        nonlocal C
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        C -= 1

    def add_edge(u, w):
        nonlocal E
        activate(u)
        activate(w)
        union(u, w)
        E += 1

    def add_h(x, y):
        # horizontal edge at (x,y): (x,y)-(x+1,y)
        idx = y * cols + x
        if h[idx]:
            return
        h[idx] = 1
        add_edge(vid(x, y), vid(x + 1, y))

    def add_v(x, y):
        # vertical edge at (x,y): (x,y)-(x,y+1)
        idx = x * (rows - 1) + y
        if v[idx]:
            return
        v[idx] = 1
        add_edge(vid(x, y), vid(x, y + 1))

    # unit edges for each character in local coords (0..2, 0..4)
    # ('h', x, y): horizontal unit edge from (x,y) to (x+1,y) with x in {0,1}
    # ('v', x, y): vertical unit edge from (x,y) to (x,y+1) with y in {0,1,2,3}
    char_edges = {
        '2': (('h',0,0),('h',1,0), ('v',2,0),('v',2,1),
              ('h',0,2),('h',1,2), ('v',0,2),('v',0,3), ('h',0,4),('h',1,4)),
        '5': (('h',0,0),('h',1,0), ('v',0,0),('v',0,1),
              ('h',0,2),('h',1,2), ('v',2,2),('v',2,3), ('h',0,4),('h',1,4)),
        '[': (('h',0,0),('h',1,0), ('v',0,0),('v',0,1),('v',0,2),('v',0,3), ('h',0,4),('h',1,4)),
        ']': (('h',0,0),('h',1,0), ('v',2,0),('v',2,1),('v',2,2),('v',2,3), ('h',0,4),('h',1,4)),
    }

    for i, ch in enumerate(s):
        base = 2 * i
        for typ, x, y in char_edges[ch]:
            if typ == 'h':
                add_h(base + x, y)
            else:
                add_v(base + x, y)

    # bounded faces = E - V + C
    print(E - V + C)

if __name__ == "__main__":
    solve()
