def main():
    import sys
    S = sys.stdin.readline().strip()     # 산지니 아이디
    T = sys.stdin.readline().strip()     # 출력해야 할 문자열

    banned = set(S)                      # 제거할 문자 집합
    result = [ch for ch in T if ch not in banned]
    print(''.join(result))

if __name__ == '__main__':
    main()
