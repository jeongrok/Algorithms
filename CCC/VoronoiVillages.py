# ccc18s1

n = int(input())
position = []
for i in range(n):
    position.append(int(input()))

position.sort()

min_size = ((position[2] - position[0]) / 2)

for i in range(2 , n-1):
    size = (position[i+1] - position[i-1]) / 2
    if size < min_size:
        min_size = size

min_size = round(min_size,2)
print(min_size)