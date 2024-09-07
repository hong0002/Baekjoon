# 입력 받기
t = int(input())  # 테스트 케이스의 수

# 각 테스트 케이스에 대해 처리
for _ in range(t):
    text = input()  # 한 줄의 텍스트 입력
    print(text[::-1])  # 텍스트를 역순으로 출력
