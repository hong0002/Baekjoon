def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    output_lines = []
    index = 1
    
    for i in range(1, t + 1):
        # 세 변의 길이를 읽어서 정수 리스트로 변환한 후 정렬합니다.
        sides = list(map(int, input_data[index:index+3]))
        index += 3
        sides.sort()
        # 직각삼각형 판별: 작은 두 변의 제곱의 합과 가장 긴 변의 제곱이 같으면 직각삼각형입니다.
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            output_lines.append(f"Case #{i}: YES")
        else:
            output_lines.append(f"Case #{i}: NO")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == '__main__':
    solve()
