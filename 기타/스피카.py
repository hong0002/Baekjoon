import sys

def main():
    adj = [set() for _ in range(13)]  # 1..12
    for _ in range(12):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].add(y)
        adj[y].add(x)

    deg = [0] * 13
    for i in range(1, 13):
        deg[i] = len(adj[i])

    for i in range(1, 13):
        if deg[i] == 3:
            neigh_degs = sorted(deg[j] for j in adj[i])
            if neigh_degs == [1, 2, 3]:
                print(i)
                return

if __name__ == "__main__":
    main()
