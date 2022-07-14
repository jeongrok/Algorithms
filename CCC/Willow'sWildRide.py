#ecoo18r1p1
for i in range(10):
    data = list(map(int, input().split()))
    count = 0
    lst = []
    for i in range(data[1]):
        lst.append(input())
    for i in range(len(lst)):
        if lst[i] == "B":
            count += data[0]
        if count > 0:
            count -= 1
    print(count)