import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    clap = 0

    for i in range(1, N+1):
        for c in str(i):
            if c in ('3', '6', '9'):
                clap += 1

    print(clap)

if __name__ == "__main__":
    main()
