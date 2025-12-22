import sys

def main():
    counts = {}
    order = []
    total = 0

    for line in sys.stdin:
        name = line.rstrip('\n')
        if name == "0":
            break
        if name not in counts:
            counts[name] = 0
            order.append(name)
        counts[name] += 1
        total += 1

    out_lines = []
    for name in order:
        out_lines.append(f"{name}: {counts[name]}")
    out_lines.append(f"Grand Total: {total}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
