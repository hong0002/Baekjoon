# 입력 받기
import sys
input = sys.stdin.read

# 데이터를 읽고 처리
data = input().splitlines()
N = int(data[0])
results = []

for i in range(1, N + 1):
    P, C = map(float, data[i].split())
    # 원래 가격 O를 계산
    O = P / (C / 100 + 1)
    # 결과 저장
    results.append(f"{O:.9f}")

# 결과 출력
print("\n".join(results))
