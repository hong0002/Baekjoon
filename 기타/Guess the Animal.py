import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    idx = 1

    animals = []
    for _ in range(n):
        name = data[idx]      # 이름 (사용 안 함)
        idx += 1
        k = int(data[idx])
        idx += 1
        traits = set(data[idx:idx+k])
        idx += k
        animals.append(traits)

    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            common = len(animals[i] & animals[j])
            if common > best:
                best = common

    # 최대 공통 개수 + 1
    print(best + 1)

if __name__ == "__main__":
    main()
