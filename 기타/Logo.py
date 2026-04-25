import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    x, y = 0.0, 0.0
    angle = 0.0  # degree
    
    for _ in range(n):
        cmd, val = input().split()
        val = float(val)
        
        if cmd == 'fd':
            x += val * math.cos(math.radians(angle))
            y += val * math.sin(math.radians(angle))
        elif cmd == 'bk':
            x -= val * math.cos(math.radians(angle))
            y -= val * math.sin(math.radians(angle))
        elif cmd == 'lt':
            angle += val
        elif cmd == 'rt':
            angle -= val
    
    dist = math.sqrt(x**2 + y**2)
    print(round(dist))
