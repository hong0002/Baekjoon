def main():
    import sys
    input = sys.stdin.readline

    # 하드코딩된 스코어보드 데이터
    # [풀이 개수, [풀이한 문제 리스트(사전 순)]]
    # 출처: Velog 블로그 (minco777) :contentReference[oaicite:0]{index=0}
    Score_Board = [
        [11, ["A","B","C","D","E","F","G","H","J","L","M"]],  # 1등 AKARAKA
        [9,  ["A","C","E","F","G","H","I","L","M"]],          # 2등 goraani
        [9,  ["A","C","E","F","G","H","I","L","M"]],          # 3등 Raa_FanClub
        [9,  ["A","B","C","E","F","G","H","L","M"]],          # 4등 입대 전 라스트댄스
        [8,  ["A","C","E","F","G","H","L","M"]],              # 5등 진짜1등하러왔습니다
        [8,  ["A","C","E","F","G","H","L","M"]],              # 6등 돈비고고고
        [8,  ["A","C","E","F","G","H","L","M"]],              # 7등 가지오이당근
        [8,  ["A","C","E","F","G","H","L","M"]],              # 8등 병공병
        [8,  ["A","C","E","F","G","H","L","M"]],              # 9등 기령손
        [8,  ["A","B","C","F","G","H","L","M"]],              # 10등 홍하예프
    ]

    N = int(input().strip())
    solved_count, problems = Score_Board[N-1]

    # 1) 푼 문제 수
    print(solved_count)
    # 2) 사전 순(이미 저장된 순서가 사전 순입니다)
    print(" ".join(problems))


if __name__ == "__main__":
    main()
