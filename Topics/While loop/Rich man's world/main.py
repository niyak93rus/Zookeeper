initial_deposit = int(input())
years = 0

while initial_deposit < 700000:
    initial_deposit *= 1.071
    years += 1
print(years)
