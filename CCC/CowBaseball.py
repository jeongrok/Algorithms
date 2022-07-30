#USACO 201312

# using sorting
# and then using binary search
from bisect import bisect_left, bisect_right


n = int(input())

position = []
for i in range(n):
    position.append(int(input()))

position.sort()
total = 0

for i in range(n):
    for j in range(i+1, n):
        diff = position[j] - position[i]
        low = position[j] + diff
        high = position[j] + diff * 2
        # linear search using while loop
        left = j + 1
        while left < n and position[left] < low:
            left += 1
        right = left
        while right < n and position[right] <= high:
            right += 1
        # using binary search
        # left = bisect_left(position, low)
        # right = bisect_right(position,high)
        total += right - left

print(total)


