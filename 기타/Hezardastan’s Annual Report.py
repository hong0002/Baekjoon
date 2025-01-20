def calculate_min_sheets(n, chapters):
    total_pages = 0
    for pages in chapters:
        total_pages += pages
        if pages % 2 == 1:  # Add a blank page for odd-numbered chapters
            total_pages += 1

    # Each sheet contains 2 pages
    return (total_pages + 1) // 2

# 입력 처리
n = int(input().strip())
chapters = list(map(int, input().split()))

# 결과 출력
print(calculate_min_sheets(n, chapters))
