import sys

def main():
    input = sys.stdin.readline

    my_name, my_pref, max_dist = input().split()
    max_dist = int(max_dist)

    n = int(input().strip())
    res = []

    for _ in range(n):
        name, gender, dist = input().split()
        dist = int(dist)

        if dist <= max_dist:
            if len(my_pref) == 2 or gender == my_pref:
                res.append(name)

    if not res:
        print("No one yet")
    else:
        res.sort()
        print("\n".join(res))

if __name__ == "__main__":
    main()
