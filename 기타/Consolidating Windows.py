import math

# Sisendi lugemine
a, b = map(int, input().split())

# Arvutame suure ruudu külje pikkuse
c = math.sqrt(a**2 + b**2)

# Väljundi kuvamine vastava täpsusega
print(f"{c:.12f}")
