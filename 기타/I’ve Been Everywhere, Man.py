import sys

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        cities = set()
        for _ in range(n):
            cities.add(input().strip())
        print(len(cities))

if __name__ == "__main__":
    main()
