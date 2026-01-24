import sys

def main():
    H, S = map(int, sys.stdin.readline().split())

    if H <= 2:
        print(1)
        return

    if H <= 4:   # H == 3 or 4
        T = H + 2 * S
    else:        # H >= 5
        T = H + 3 * S

    print((T + 1) // 2)

if __name__ == "__main__":
    main()
