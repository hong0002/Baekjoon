def calculate_population(p, t):
    # 사망하는 인구 수
    deaths = t // 7
    # 태어나는 인구 수
    births = t // 4
    # 최종 인구 계산
    final_population = p + births - deaths
    return final_population

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    results = []
    
    index = 1
    for _ in range(n):
        p = int(data[index])
        t = int(data[index + 1])
        index += 2
        result = calculate_population(p, t)
        results.append(result)
    
    for result in results:
        print(result)

# 함수 호출
main()
