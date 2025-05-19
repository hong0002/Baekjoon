import sys

def is_ladder(words):
    # 인접한 단어 쌍마다 길이와 한 글자 차이 여부 검사
    for w1, w2 in zip(words, words[1:]):
        if len(w1) != len(w2):
            return False
        # 해밍 거리 계산
        diff = sum(c1 != c2 for c1, c2 in zip(w1, w2))
        if diff != 1:
            return False
    return True

def main():
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == "#":
            # 빈 리스트인 경우: 모든 입력 종료
            if not words:
                break
            # 현재까지 모인 단어들로 검사
            print("Correct" if is_ladder(words) else "Incorrect")
            words = []
        else:
            words.append(line)

if __name__ == "__main__":
    main()
