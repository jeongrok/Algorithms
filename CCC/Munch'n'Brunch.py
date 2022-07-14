# ecoo17r1p1
for i in range(10):
    cost = int(input())
    # proportion = input()
    # prop = proportion.split()
    # for i in range(len(prop)):
    #     prop[i] = float(prop[i])
    # lines above can be simplified as
    prop = list(map(float, input().split()))
    students = int(input())
    result = 0

    for i in range(len(prop)):
        prop[i] = int(prop[i] * students)

    # have to consider the case where the dropped students
    # due to decimal points do not add up to the variable students
    counted = sum(prop)
    uncounted = students - counted
    most = max(prop)
    where = prop.index(most)
    prop[where] += uncounted

    result += 6 * prop[0] + 5 * prop[1] + 3.5 * prop[2] + 2.5 * prop[3]

    if result < cost:
        print("YES")
    else:
        print("NO")