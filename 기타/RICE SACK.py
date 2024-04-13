# 각 케이스에 대한 입력을 받는 함수
def get_input():
    num_cases = int(input())  # 케이스 수 입력
    cases = []  # 케이스를 저장할 리스트

    # 케이스 수 만큼 반복하여 입력 받음
    for _ in range(num_cases):
        case = list(map(int, input().split()))  # 각 케이스의 5개 무게를 리스트로 변환하여 저장
        cases.append(case)  # 현재 케이스를 리스트에 추가
    
    return num_cases, cases  # 케이스 수와 케이스 리스트를 반환

# 주어진 조건에 맞게 최대 무게를 찾는 함수
def find_heaviest_sack(num_cases, cases):
    for i in range(num_cases):
        heaviest = max(cases[i])  # 현재 케이스에서 가장 무거운 무게를 찾음
        print(f"Case #{i+1}: {heaviest}")  # 케이스 번호와 가장 무거운 무게를 출력

# 메인 함수
def main():
    num_cases, cases = get_input()  # 입력 받기
    find_heaviest_sack(num_cases, cases)  # 최대 무게 찾기

if __name__ == "__main__":
    main()  # 메인 함수 호출
