def max_planets_to_visit(n, m):
    if abs(n - m) <= 1:
        return n + m
    else:
        return 2 * min(n, m) + 1

# Пример использования:
n, m = map(int, input().split())
print(max_planets_to_visit(n, m))
