def count_spheres(n):
    # 전체 구의 개수 계산
    result = n * (n + 1) * (n + 2) // 6
    print(result)

# 예제 실행
if __name__ == "__main__":
    n = int(input())  # 입력받기
    count_spheres(n)
