import math

n, a, b = map(int, input().split())
l = a * b // math.gcd(a, b)

count_fb = n // l
count_f  = n // a - count_fb
count_b  = n // b - count_fb

print(count_f, count_b, count_fb)
