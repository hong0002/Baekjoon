def count_finger_ways(n: int) -> int:
    ans = 0
    # a: 첫째 손 (0~5), b: 둘째 손 (0~a)
    for a in range(0, 6):
        for b in range(0, a+1):
            if a + b == n:
                ans += 1
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    print(count_finger_ways(n))
