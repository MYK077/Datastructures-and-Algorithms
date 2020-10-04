
# Given a non-empty 2D array grid of 0's and 1's, 
# an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, 
# because the island must be connected 4-directionally.
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area,self.searchMaximumArea(grid, row, col))
        return area
    
    def searchMaximumArea(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 0
        area =  1
        area += self.searchMaximumArea(grid,row+1,col)
        area += self.searchMaximumArea(grid,row-1,col)
        area += self.searchMaximumArea(grid,row,col+1)
        area += self.searchMaximumArea(grid,row,col-1)
        
        return area

a = Solution()
print(a.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))