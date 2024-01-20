def remove_substring(s, i, j):
    return s[:i] + s[j:]

# 입력 받기
n = int(input())
for _ in range(n):
    data = input().split()
    string, i, j = data[0], int(data[1]), int(data[2])
    
    # 결과 출력
    result = remove_substring(string, i, j)
    print(result)
