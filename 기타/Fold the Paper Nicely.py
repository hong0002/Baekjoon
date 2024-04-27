def final_sizes(width, height, folds):
    for _ in range(folds):
        if width >= height:
            width //= 2
        else:
            height //= 2
    return max(width, height), min(width, height)

# 테스트 케이스 수 입력 받기
n = int(input())

for i in range(n):
    # 테스트 케이스 입력 받기
    width, height, folds = map(int, input().split())
    
    # 테스트 케이스 출력 포맷에 맞게 출력하기
    print("Data set:", width, height, folds)
    final_width, final_height = final_sizes(width, height, folds)
    print(final_width, final_height)
    print()  # 공백 라인 출력
