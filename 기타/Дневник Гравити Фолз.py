def count_pages(w, h, n, a, b):
    # 글자가 페이지에 들어갈 수 없는 경우
    if a > w or b > h:
        return -1

    # 한 페이지에 들어갈 수 있는 글자 수 계산
    letters_per_page = (w // a) * (h // b)
    
    # 필요한 페이지 수 계산
    pages_needed = (n + letters_per_page - 1) // letters_per_page
    
    return pages_needed

# 입력값 읽기
w, h = map(int, input().split())
n, a, b = map(int, input().split())

# 결과 출력
print(count_pages(w, h, n, a, b))
