#USACO 201612 Silver
n = int(input())
combi_to_num = {}

for i in range(n):
    lst = input().split()
    city = lst[0][:2]
    state = lst[1]
    if city != state:
        combo = city + state
        if not combo in combi_to_num:
            combi_to_num[combo] = 1
        else:
            combi_to_num[combo] += 1

total = 0
for combo in combi_to_num:
    other_combo = combo[2:] + combo[:2]
    if other_combo in combi_to_num:
        total += combi_to_num[combo] * combi_to_num[other_combo]

total //= 2
print(total)