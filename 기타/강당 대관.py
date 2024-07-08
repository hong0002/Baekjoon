def find_max_seminar():
    seminars = {}
    
    for _ in range(7):
        line = input().split()
        seminar_name = line[0]
        attendees = int(line[1])
        seminars[seminar_name] = attendees
    
    max_seminar = max(seminars, key=seminars.get)
    print(max_seminar)

if __name__ == "__main__":
    find_max_seminar()
