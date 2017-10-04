class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        table = {}
        return self.rec(obstacleGrid, 0, 0, table)
    
    def rec(self, grid, i, j, table):
        if grid[i][j] != 0:
            return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        if (i, j) in table:
            return table[(i, j)]
        res = 0
        if i < len(grid) - 1 and grid[i + 1][j] == 0:
            res += self.rec(grid, i + 1, j, table)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
            res += self.rec(grid, i, j + 1, table)
        table[(i, j)] = res
        return res