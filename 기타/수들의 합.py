S = int(input().strip())
# 부동소수 사용해도 되지만, 안전하게 이분 탐색으로도 가능
lo, hi = 0, 2_000_000_000  # 충분히 큰 상한
while lo < hi:
    mid = (lo + hi + 1) // 2
    if mid * (mid + 1) // 2 <= S:
        lo = mid
    else:
        hi = mid - 1
print(lo)
