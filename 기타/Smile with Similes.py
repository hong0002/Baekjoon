# 입력 처리
n = int(input())  # 형용사의 개수
m = int(input())  # 명사의 개수

adjectives = [input().strip() for _ in range(n)]  # n개의 형용사 입력 받기
nouns = [input().strip() for _ in range(m)]  # m개의 명사 입력 받기

# 모든 가능한 조합 출력
for adj in adjectives:
    for noun in nouns:
        print(f"{adj} as {noun}")
