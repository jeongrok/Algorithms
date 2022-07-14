#ccc07j3

cash=[100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

n = int(input())

removal = []
for i in range(n):
    removal.append(int(input()))

for i in removal:
    cash[i - 1] = 0

avg = 0
for i in range(len(cash)):
    avg += cash[i]

avg = avg / (10 - len(removal))

if avg > int(input()):
    print("no deal")
else:
    print("deal")
