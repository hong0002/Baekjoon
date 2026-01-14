import sys

def main():
    S = int(sys.stdin.readline().strip())  # high speed rail time
    F = int(sys.stdin.readline().strip())  # flight time (station-airport 이동 무시)

    if F < S:
        print("flight")
    else:
        print("high speed rail")

if __name__ == "__main__":
    main()
