def count_mismatches(S: str) -> int:
    target = "SciComLove"
    # zip으로 두 문자열을 묶어 한 글자씩 비교하여 불일치 개수를 센다
    return sum(1 for a, b in zip(S, target) if a != b)

if __name__ == "__main__":
    S = input().rstrip()
    print(count_mismatches(S))
