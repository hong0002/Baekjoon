# 첫 번째 줄에서 N을 입력받음
N = int(input())

# N개의 숫자에 대해 반복
for _ in range(N):
    # 각 숫자를 문자열로 입력받고 자릿수를 구하여 출력
    number = input().strip()
    print(len(number))
