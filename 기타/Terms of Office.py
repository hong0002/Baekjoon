# 입력받은 X와 Y
X = int(input())
Y = int(input())

# 60년마다 모든 직책이 바뀜
for year in range(X, Y + 1, 60):
    print("All positions change in year", year)
