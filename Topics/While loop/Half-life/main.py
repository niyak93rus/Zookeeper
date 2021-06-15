initial = int(input())
final = int(input())

periods = 0
days = 0

while initial > final:
    initial /= 2
    periods += 1
days = periods * 12
print(days)
