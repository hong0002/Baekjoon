import sys
import math

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # number of figures
    max_volume = 0
    pi = 3.14159
    
    for i in range(1, n + 1):
        line = data[i].split()
        figure_type = line[0]
        
        if figure_type == "S":  # Sphere
            r = float(line[1])
            volume = (4/3) * pi * (r ** 3)
        elif figure_type == "C":  # Cone
            r = float(line[1])
            h = float(line[2])
            volume = (1/3) * pi * (r ** 2) * h
        elif figure_type == "L":  # Cylinder
            r = float(line[1])
            h = float(line[2])
            volume = pi * (r ** 2) * h
        
        if volume > max_volume:
            max_volume = volume
    
    print(f"{max_volume:.3f}")

if __name__ == "__main__":
    main()
