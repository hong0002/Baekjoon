import sys

def main():
    input = sys.stdin.readline

    n = int(input().strip())
    YEAR = 365 * 24 * 60
    DAY = 24 * 60
    HOUR = 60

    for _ in range(n):
        line = input().rstrip("\n")
        # game title can contain commas? problem statement shows one comma separator.
        # We'll split from the right to be safe.
        title, minutes_str = line.rsplit(",", 1)
        m = int(minutes_str)

        years = m // YEAR
        m %= YEAR
        days = m // DAY
        m %= DAY
        hours = m // HOUR
        m %= HOUR
        minutes = m

        parts = [f"{title} -"]
        if years > 0:
            parts.append(f"{years} year(s)")
        if days > 0:
            parts.append(f"{days} day(s)")
        if hours > 0:
            parts.append(f"{hours} hour(s)")
        if minutes > 0:
            parts.append(f"{minutes} minute(s)")

        print(" ".join(parts))

if __name__ == "__main__":
    main()
