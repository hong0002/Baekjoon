def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    while True:
        N = int(data[index])
        D = int(data[index + 1])
        index += 2
        
        if N == 0 and D == 0:
            break
        
        # Initialize attendance list for all alumni
        full_attendance = [True] * N
        
        for _ in range(D):
            attendees = data[index:index + N]
            index += N
            # Update each alumnus's full attendance record
            for i in range(N):
                if attendees[i] == '0':
                    full_attendance[i] = False
        
        # Check if there is at least one alumnus with full attendance
        if any(full_attendance):
            results.append('yes')
        else:
            results.append('no')
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
