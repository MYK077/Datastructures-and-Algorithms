# Zero Matrix: Write an algorithm such that if an 
# element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        r, c = set(), set()

        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == 0:
                    r.add(x)
                    c.add(y)

        for x in range(rows):
            for y in range(cols):
                if x in r or y in c:
                    matrix[x][y] = 0
        return matrix


obj = Solution()
print(obj.setZeroes([[2, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
