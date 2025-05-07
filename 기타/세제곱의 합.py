def main():
    N = int(input().strip())
    # 1부터 N까지의 합
    s = N * (N + 1) // 2
    # 1부터 N까지의 합을 제곱한 값
    s2 = s * s
    # 1부터 N까지의 세제곱의 합 (공식에 의해 s2와 동일)
    # cube_sum = (N * (N + 1) // 2) ** 2
    cube_sum = s2

    print(s)
    print(s2)
    print(cube_sum)

if __name__ == "__main__":
    main()
