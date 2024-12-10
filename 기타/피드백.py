# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
N = int(input())

# 수열 생성
A = [1]  # 첫 번째 요소
A.append(2)  # 두 번째 요소는 반드시 2

# 나머지 요소 생성 (1부터 1000까지 순회하며 추가)
current = 3
while len(A) < N - 1:  # 마지막 값을 제외한 나머지 채우기
    if current > A[-1]:  # 증가 조건 확인
        A.append(current)
    current += 1

# 마지막 요소는 소수 중에서 선택
for candidate in range(current, 1001):
    if is_prime(candidate):
        A.append(candidate)
        break

# 출력
print(N)
print(" ".join(map(str, A)))
