# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example :

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

from collections import deque


class Solution():
    q = deque()
    visited = set()
    # directions up, down, right, left
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def visitZeros(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    self.q.append((row, col))
                    self.visited.add((row, col))

    def findMinDistance(self, matrix):
        while self.q:
            x, y = self.q.popleft()
            for dir in self.dirs:
                newX, newY = x+dir[0], y+dir[1]
                if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 \
                        and (newX, newY) not in self.visited:
                    matrix[newX][newY] = matrix[x][y] + 1
                    self.q.append((newX, newY))
                    self.visited.add((newX, newY))
        return matrix


input = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
a = Solution()
a.visitZeros(input)
print(a.findMinDistance(input))
