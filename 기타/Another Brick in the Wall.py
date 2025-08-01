def will_complete(h: int, w: int, bricks: list[int]) -> bool:
    layers = 0
    width = 0
    for x in bricks:
        width += x
        if width == w:
            layers += 1
            width = 0
            if layers == h:
                return True
        elif width > w:
            return False
    return False  # 벽돌이 다 떨어졌는데도 h층 못 채웠으면 실패

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    h, w, n = map(int, data[:3])
    bricks = list(map(int, data[3:3+n]))
    print("YES" if will_complete(h, w, bricks) else "NO")
