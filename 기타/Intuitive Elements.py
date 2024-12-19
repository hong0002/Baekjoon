# 입력 받기
t = int(input())  # 테스트 케이스 수
results = []

for _ in range(t):
    a = input().strip()  # 문자열 a
    b = input().strip()  # 약어 b

    # b의 모든 문자가 a에 포함되는지 확인
    if all(char in a for char in b):
        results.append("YES")
    else:
        results.append("NO")

# 결과 출력
print("\n".join(results))
