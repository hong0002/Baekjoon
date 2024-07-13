import sys
import random

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    menus = data[1:]
    
    # 무작위로 메뉴 하나 선택
    selected_menu = random.choice(menus)
    dishes = selected_menu.split()[1:]  # 첫 번째 숫자를 제외하고 나머지 부분
    
    # 출력
    print(len(dishes))
    for dish in dishes:
        print(dish)

if __name__ == "__main__":
    main()
