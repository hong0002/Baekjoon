import math

t = int(input())
for _ in range(t):
    result = 0
    points = list(map(int, input().split()))
    result += math.trunc(9.23076 * (26.7 - points[0])**1.835)
    result += math.trunc(1.84523 * (points[1] - 75)**1.348)
    result += math.trunc(56.0211 * (points[2] - 1.5)**1.05)
    result += math.trunc(4.99087 * (42.5 - points[3])**1.81)
    result += math.trunc(0.188807 * (points[4] - 210)**1.41)
    result += math.trunc(15.9803 * (points[5] - 3.8)**1.04)
    result += math.trunc(0.11193 * (254 - points[6])**1.88)
    print(result)
