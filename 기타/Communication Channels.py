def check_transmissions(T, transmissions):
    results = []
    for i in range(T):
        input_str, output_str = transmissions[i]
        if input_str == output_str:
            results.append("OK")
        else:
            results.append("ERROR")
    return results

# 입력 받기
T = int(input())
transmissions = [input().split() for _ in range(T)]

# 결과 출력
results = check_transmissions(T, transmissions)
for result in results:
    print(result)
