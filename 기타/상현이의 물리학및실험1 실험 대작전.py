import sys
input = sys.stdin.readline

def count_materials(N, E, densities):
    densities.sort()
    count = 1  # 첫 번째 추는 항상 첫 번째 물질
    for i in range(1, N):
        if densities[i] - densities[i-1] >= E:
            count += 1
    return count

def main():
    N, E = map(int, input().split())
    D = list(map(int, input().split()))
    print(count_materials(N, E, D))

if __name__ == "__main__":
    main()
