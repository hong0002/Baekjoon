def calculate_total_strokes():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    S = data[1]
    
    stroke_counts = {'j': 2, 'o': 1, 'i': 2}
    total_strokes = 0
    
    for char in S:
        total_strokes += stroke_counts[char]
    
    print(total_strokes)

if __name__ == "__main__":
    calculate_total_strokes()
