n = int(input())

def days_covered(intervals, fired):
    covered = set()
    for i in range(len(intervals)):
        if i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)
    return(len(covered))


total = []
for i in range(n):
    days = [int(value) for value in input().split()]
    total.append(days)

max = 0
for i in range(len(total)):
    result = days_covered(total, i)
    if result > max:
        max = result

print(max)