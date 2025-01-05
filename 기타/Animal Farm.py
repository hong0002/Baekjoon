def max_influence(n, animals):
    pigs = []
    non_pigs = []
    
    # 동물들을 피그와 비 피그로 나누기
    for species, influence in animals:
        if species == "pig":
            pigs.append(influence)
        else:
            non_pigs.append((species, influence))
    
    # 피그 중 가장 큰 영향력 찾기
    max_pig_influence = max(pigs)
    
    # 비 피그 동물 중 피그보다 작은 영향력들만 선택
    total_influence = max_pig_influence  # 피그의 영향력 포함
    for species, influence in non_pigs:
        if influence < max_pig_influence:
            total_influence += influence
    
    return total_influence

# 입력 처리
n = int(input())
animals = [input().split() for _ in range(n)]
animals = [(species, int(influence)) for species, influence in animals]

# 결과 출력
print(max_influence(n, animals))
