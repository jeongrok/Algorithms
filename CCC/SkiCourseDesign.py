def cost_for_range(heights, min):
    cost = 0
    for height in heights:
        if height < min:
            cost += (min - height) ** 2
        elif height > min + 17:
            cost += (min + 17 - height) ** 2
    return cost

n = int(input())

heights = []
for i in range(n):
    heights.append(int(input()))

min_cost = cost_for_range(heights, 0)

for i in range(1, 101):
    result = cost_for_range(heights, i)
    if result < min_cost:
        min_cost = result

print(min_cost)
