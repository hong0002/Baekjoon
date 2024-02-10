def check_twins(jersey_numbers):
    mack_present = 18 in jersey_numbers
    zack_present = 17 in jersey_numbers

    if mack_present and zack_present:
        return "both"
    elif mack_present:
        return "mack"
    elif zack_present:
        return "zack"
    else:
        return "none"

def main():
    n = int(input())  # 입력 데이터 세트의 개수

    for _ in range(n):
        jersey_numbers = list(map(int, input().split()))
        print(" ".join(map(str, jersey_numbers)))
        result = check_twins(jersey_numbers)
        print(result + "\n")

if __name__ == "__main__":
    main()
