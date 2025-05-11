def main():
    import sys
    input = sys.stdin.readline

    a, b = map(int, input().split())
    c, d = map(int, input().split())
    t = int(input())

    D = abs(a - c) + abs(b - d)
    if t >= D and (t - D) % 2 == 0:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
