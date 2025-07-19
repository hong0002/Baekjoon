import sys

def main():
    for line in sys.stdin:
        A = int(line)
        # 6의 배수인지 확인
        print("Y" if A % 6 == 0 else "N")

if __name__ == "__main__":
    main()
