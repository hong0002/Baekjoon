import sys

def better(d1, p1, d2, p2):
    # return True if (d1,p1) is better value (smaller P/D^2) than (d2,p2)
    return p1 * (d2 * d2) < p2 * (d1 * d1)

def main():
    input = sys.stdin.readline
    menu_idx = 1

    while True:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        best_d, best_p = None, None
        for _ in range(n):
            d, p = map(int, input().split())
            if best_d is None or better(d, p, best_d, best_p):
                best_d, best_p = d, p

        print(f"Menu {menu_idx}: {best_d}")
        menu_idx += 1

if __name__ == "__main__":
    main()
