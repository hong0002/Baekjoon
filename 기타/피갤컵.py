N = int(input())

total_month = 2024 * 12 + (8 - 1) + (N - 1) * 7
year = total_month // 12
month = total_month % 12 + 1

print(year, month)
