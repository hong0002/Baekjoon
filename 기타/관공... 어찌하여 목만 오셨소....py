# 용의자 수 입력
N = int(input())

# 용의자 이름 중에서 관우를 죽인 범인을 찾기
for _ in range(N):
    name = input()
    if 'S' in name:
        print(name)
        break
