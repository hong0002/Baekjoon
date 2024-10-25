import sys
input = sys.stdin.read

# 입력 받기
data = input().split()
T = int(data[0])
results = []

# 각 테스트 케이스에 대해 처리
for i in range(1, T + 1):
    N = int(data[i])
    results.append(N * N)

# 결과 출력
sys.stdout.write("\n".join(map(str, results)) + "\n")
