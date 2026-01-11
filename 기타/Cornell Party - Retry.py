import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); m = int(data[idx + 1])
        idx += 2

        s = set()

        # Cornell names
        for _ in range(n):
            s.add(data[idx].decode())
            idx += 1

        # White names
        for _ in range(m):
            s.add(data[idx].decode())
            idx += 1

        out.append(str(len(s)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
