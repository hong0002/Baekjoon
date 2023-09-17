persons = list(map(int, input().split()))
persons.sort()
print(abs((persons[0]+persons[3]) - (persons[1]+persons[2])))
