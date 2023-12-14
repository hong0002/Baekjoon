def find_answer(n):
    remainder = n % 8
    
    if remainder == 1:
        return 1
    elif remainder == 0 or remainder == 2:
        return 2
    elif remainder == 3 or remainder == 7:
        return 3
    elif remainder == 4 or remainder == 6:
        return 4
    elif remainder == 5:
        return 5

def main():
    n = int(input())
    answer = find_answer(n)
    print(answer)

if __name__ == "__main__":
    main()
