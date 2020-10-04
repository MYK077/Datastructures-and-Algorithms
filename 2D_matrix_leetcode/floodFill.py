# An image is represented by a 2-D array of integers, 
# each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
# and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), 
# and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.
# Example 1:
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        
        rows = len(image)
        cols = len(image[0])
        
        color = image[sr][sc]
        
        if color == newColor: return image
        
        for i in range(rows):
            for j in range(cols):
                if i == sr and j == sc:
                    self.fillColor(image, sr, sc, color, newColor)
                    return image
        
    def fillColor(self, image, row, col, color, newColor):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] == newColor or \
        image[row][col] != color:
            return
        if image[row][col] == color:
            image[row][col] = newColor
        self.fillColor(image, row+1, col, color, newColor)
        self.fillColor(image, row-1, col, color, newColor)
        self.fillColor(image, row, col+1, color, newColor)
        self.fillColor(image, row, col-1, color, newColor)

fill = Solution()
print(fill.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))