def triangular_number(n):
    return n * (n + 1) // 2

def weighted_sum_of_triangular_numbers(n):
    W_n = 0
    for k in range(1, n + 1):
        T_k_plus_1 = triangular_number(k + 1)
        W_n += k * T_k_plus_1
    return W_n

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    test_cases = [int(data[i]) for i in range(1, T + 1)]
    
    results = [weighted_sum_of_triangular_numbers(n) for n in test_cases]
    
    for result in results:
        print(result)

# 이 코드는 표준 입력을 통해 데이터를 받습니다.
# 입력을 직접 제공해야 하는 경우 아래 코드를 통해 직접 입력할 수 있습니다.
if __name__ == "__main__":
    main()
