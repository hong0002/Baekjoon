import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    total = 0

    for line in lines:
        kind, x = line.split()
        x = int(x)
        if kind == "Stair":
            total += x * 17
        else:  # "Es"
            total += x * 21

    print(total)

if __name__ == "__main__":
    main()
