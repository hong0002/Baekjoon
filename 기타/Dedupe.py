# 중복 문자를 제거하는 함수
def remove_redundancy(s):
    result = []
    for char in s:
        # 현재 문자가 결과 리스트의 마지막 문자와 같지 않으면 추가
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

# 데이터 세트의 개수 입력
num_datasets = int(input())

# 각 데이터 세트에 대해 중복 문자 제거 후 출력
for _ in range(num_datasets):
    input_string = input()
    deduped_string = remove_redundancy(input_string)
    print(deduped_string)
