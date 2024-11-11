# 입력 받기
Dusa_size = int(input().strip())
while True:
    try:
        yobi_size = int(input().strip())
        
        # Yobi 크기에 따른 처리
        if yobi_size < Dusa_size:
            Dusa_size += yobi_size
        else:
            print(Dusa_size)
            break
    except EOFError:
        break
