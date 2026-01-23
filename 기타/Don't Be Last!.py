import sys

def main():
    input = sys.stdin.readline

    cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
    total = {name: 0 for name in cows}

    n = int(input().strip())
    for _ in range(n):
        name, milk = input().split()
        total[name] += int(milk)

    values = list(total.values())
    m = min(values)

    # m보다 큰 생산량들 중 최소값 찾기
    bigger = sorted({v for v in values if v > m})
    if not bigger:
        print("Tie")
        return

    second = bigger[0]
    winners = [name for name in cows if total[name] == second]

    if len(winners) == 1:
        print(winners[0])
    else:
        print("Tie")

if __name__ == "__main__":
    main()
