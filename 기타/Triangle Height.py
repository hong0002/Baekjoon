def calculate_triangle_heights():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # 첫 번째 줄은 n 값 (입력의 수)
    
    for i in range(1, n + 1):
        area, base = map(float, data[i].split())
        height = (2 * area) / base
        print(f"The height of the triangle is {height:.2f} units")

if __name__ == "__main__":
    calculate_triangle_heights()
