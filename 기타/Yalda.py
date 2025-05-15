def main():
    import sys
    input = sys.stdin.readline

    b = int(input())           # Mahya의 예산
    price_watermelon = int(input())   # 수박 가격
    price_pomegranates = int(input()) # 석류 가격
    price_nuts = int(input())         # 견과류 가격

    if b >= price_watermelon:
        print("Watermelon")
    elif b >= price_pomegranates:
        print("Pomegranates")
    elif b >= price_nuts:
        print("Nuts")
    else:
        print("Nothing")

if __name__ == "__main__":
    main()
