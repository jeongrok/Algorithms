#ecoo17r3p1
for i in range(10):
    shops, days = [int(value) for value in input().split()]
    shop_total = [0] * shops
    bonus = 0
    for day in range(days):
        day_sales = [int(value) for value in input().split()]
        if sum(day_sales) % 13 == 0:
            bonus += sum(day_sales) // 13
        shop_total = [a + b for a, b in zip(shop_total, day_sales)]
        print(shop_total)
    for shop in shop_total:
        if shop % 13 == 0:
            bonus += shop // 13
    print(bonus)
    # lst = input().split()
    # shops = int(lst[0])
    # days = int(lst[1])
    # grid = []
    # bonus = 0
    # for i in range(days):
    #     row = input().split()
    #     for j in range(shops):
    #         row[j] = int(row[j])
    #     grid.append(row)
    #
    # for row in grid:
    #     total = sum(row)
    #     if total % 13 == 0 :
    #         bonus += total // 13
    #
    # for col in range(shops):
    #     total = 0
    #     for row in range(days):
    #         total += grid[row][col]
    #     if total % 13 == 0:
    #         bonus += total // 13
    # print(bonus)