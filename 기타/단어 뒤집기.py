import sys

def reverse_words(line: str) -> str:
    # 단어별로 나눈 뒤, 각 단어를 뒤집고 공백으로 합쳐서 반환
    return ' '.join(word[::-1] for word in line.split())

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        sentence = input().rstrip('\n')
        print(reverse_words(sentence))

if __name__ == '__main__':
    main()
