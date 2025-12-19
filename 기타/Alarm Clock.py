import sys

def main():
    n_line = sys.stdin.readline().strip()
    if not n_line:
        return
    n = int(n_line)

    seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # 0~9

    for h in range(24):
        for m in range(60):
            s = f"{h:02d}{m:02d}"  # "hhmm"
            total = sum(seg[int(ch)] for ch in s)
            if total == n:
                print(f"{h:02d}:{m:02d}")
                return

    print("Impossible")

if __name__ == "__main__":
    main()
