def required_elevators(zone: str, floors: int) -> int:
    if zone == "residential":
        if floors == 1:
            return 0
        elif 2 <= floors <= 5:
            return 1
        elif 6 <= floors <= 10:
            return 2
        elif 11 <= floors <= 15:
            return 3
        else:  # 16-20
            return 4

    elif zone == "commercial":
        if floors == 1:
            return 0
        elif 2 <= floors <= 7:
            return 1
        elif 8 <= floors <= 14:
            return 2
        else:  # 15-20
            return 3

    elif zone == "industrial":
        if floors == 1:
            return 0
        elif 2 <= floors <= 4:
            return 1
        elif 5 <= floors <= 8:
            return 2
        elif 9 <= floors <= 12:
            return 3
        elif 13 <= floors <= 16:
            return 4
        else:  # 17-20
            return 5

    else:
        raise ValueError(f"알 수 없는 zoning district: {zone}")

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    zone = data[0].lower()
    floors = int(data[1])
    print(required_elevators(zone, floors))
