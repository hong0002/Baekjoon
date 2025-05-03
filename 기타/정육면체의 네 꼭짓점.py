def main():
    import sys
    input = sys.stdin.readline

    # 정육면체 S의 6개 면을 인덱스 집합으로 미리 정의
    faces = [
        {0,1,2,3},  # x = 0 면
        {4,5,6,7},  # x = 1 면
        {0,1,4,5},  # y = 0 면
        {2,3,6,7},  # y = 1 면
        {0,2,4,6},  # z = 0 면
        {1,3,5,7},  # z = 1 면
    ]

    T = int(input())
    for _ in range(T):
        a, b, c, d = map(int, input().split())
        pts = {a, b, c, d}
        # 주어진 네 점이 faces 중 하나와 같으면 YES, 아니면 NO
        if any(pts == face for face in faces):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
