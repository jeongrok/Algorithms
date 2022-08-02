import heapq

class Solution(object):
def kthSmallest(self, matrix, k):

        N = len(matrix)

        minHeap = []
        for r in range(min(k,N)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)

        while k:
            element, r, c = heapq.heappop(minHeap)
            if c < N - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1

        return element


# class Solution(object):
#
#     def countLessEqual(self, matrix, mid, smaller, larger):
#
#         count, n = 0, len(matrix)
#         row, col = n - 1, 0
#
#         while row >= 0 and col < n:
#             if matrix[row][col] > mid:
#
#                 # As matrix[row][col] is bigger than the mid, let's keep track of the
#                 # smallest number greater than the mid
#                 larger = min(larger, matrix[row][col])
#                 row -= 1
#
#             else:
#
#                 # As matrix[row][col] is less than or equal to the mid, let's keep track of the
#                 # biggest number less than or equal to the mid
#
#                 smaller = max(smaller, matrix[row][col])
#                 count += row + 1
#                 col += 1
#
#         return count, smaller, larger
#
#     def kthSmallest(self, matrix, k):
#
#         n = len(matrix)
#         start, end = matrix[0][0], matrix[n - 1][n - 1]
#         while start < end:
#             mid = start + (end - start) / 2
#             smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
#
#             count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)
#
#             if count == k:
#                 return smaller
#             if count < k:
#                 start = larger  # search higher
#             else:
#                 end = smaller  # search lower
#
#         return start