import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):

        # length of the matrix
        N = len(matrix)
        # initialize the min-heap
        minHeap = []
        # add values
        for r in range(min(k, N)):
            minHeap.append((matrix[r][0], r, 0))
        # heapify
        heapq.heapify(minHeap)
        # while k > 0, pop the minimum and push the next one within the row if necessary
        while k:
            element, r, c = heapq.heappop(minHeap)
            if c < N - 1:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
            k -= 1

        return element

    def countLessEqual(self, matrix, mid, smaller, larger):

        # initializing values
        count, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

    def kthSmallest1(self, matrix, k):

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            # have a hypothetical midpoint
            mid = start + (end - start) / 2
            # initialize smaller, larger
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
            # count with the function
            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            # update numbers after function
            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start
