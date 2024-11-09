def find_children_without_gifts(n, m, k, bag1, bag2):
    all_children = set(range(1, n + 1))  # 전체 아이들의 집합 {1, 2, ..., n}
    gifted_children = set(bag1) | set(bag2)  # 첫 번째, 두 번째 주머니에 있는 아이들의 집합
    
    no_gift_children = sorted(all_children - gifted_children)  # 선물 없는 아이들의 집합에서 정렬된 리스트로 변환
    return len(no_gift_children), no_gift_children

# 입력 처리
n, m, k = map(int, input().strip().split())
bag1 = list(map(int, input().strip().split()))
bag2 = list(map(int, input().strip().split()))

# 결과 계산 및 출력
count, children = find_children_without_gifts(n, m, k, bag1, bag2)
print(count)
print(" ".join(map(str, children)))
