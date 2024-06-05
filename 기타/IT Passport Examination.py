def evaluate_exam_results(n, exam_data):
    results = []
    for data in exam_data:
        id_num, score1, score2, score3 = data
        total_score = score1 + score2 + score3
        strategy_pass = score1 >= 35 * 0.3
        management_pass = score2 >= 25 * 0.3
        technology_pass = score3 >= 40 * 0.3
        total_pass = total_score >= 55
        
        if strategy_pass and management_pass and technology_pass and total_pass:
            results.append(f"{id_num} {total_score} PASS")
        else:
            results.append(f"{id_num} {total_score} FAIL")
    
    return results

# 입력
n = int(input().strip())
exam_data = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 결과 계산 및 출력
results = evaluate_exam_results(n, exam_data)
for result in results:
    print(result)
