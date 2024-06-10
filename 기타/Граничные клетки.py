def calculate_boundary_cells(m, n):
    if m == 1 or n == 1:
        # 한 변이 1인 경우, 경계 셀은 한 변의 길이와 같다.
        return m * n
    else:
        # 전체 경계 셀의 수 계산
        boundary_cells = 2 * m + 2 * (n - 2)
        return boundary_cells

if __name__ == "__main__":
    m = int(input().strip())
    n = int(input().strip())
    result = calculate_boundary_cells(m, n)
    print(result)
