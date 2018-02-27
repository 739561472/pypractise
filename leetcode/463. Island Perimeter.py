class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for n in range(len(grid[0])):
            for m in range(len(grid)):
                if grid[m][n] == 1:
                    if n < len(grid[0])-1:
                        a = grid[m][n+1]
                    else:
                        a = 0
                    if n > 0:
                        b = grid[m][n-1]
                    else:
                        b = 0
                    if m < len(grid)-1:
                        c = grid[m+1][n]
                    else:
                        c = 0
                    if m > 0:
                        d = grid[m-1][n]
                    else:
                        d = 0
                    i = a+b+c+d
                    perimeter += (4-i)
        return perimeter