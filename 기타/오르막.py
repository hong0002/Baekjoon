import sys

def main():
    data = sys.stdin.readline().split()
    # 수가 한 개도 주어지지 않는 경우(사실 문제 제약상 없지만 안전을 위해)
    if not data:
        print("Good")
        return

    prev = int(data[0])
    for s in data[1:]:
        cur = int(s)
        if cur < prev:
            print("Bad")
            return
        prev = cur

    print("Good")

if __name__ == "__main__":
    main()
