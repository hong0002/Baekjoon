def find_level_category(level):
    if level >= 300:
        return 1
    elif level >= 275:
        return 2
    elif level >= 250:
        return 3
    else:
        return 4

# 입력 받기
N = int(input())
levels = list(map(int, input().split()))

# 결과 출력
categories = [find_level_category(level) for level in levels]
print(*categories)
