class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        table = {}
        return self.rec(grid, 0, 0, table)
    
    def rec(self, grid, i, j, table):
        if (i, j) in table:
            return table[(i, j)]
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        path1, path2 = pow(2, 32) - 1, pow(2, 32) - 1
        if i < len(grid) - 1:
            path1 = self.rec(grid, i + 1, j, table)
        if j < len(grid[0]) - 1:
            path2 = self.rec(grid, i, j + 1, table)
        minPath = min(path1, path2)
        table[(i, j)] = minPath + grid[i][j]
        return minPath + grid[i][j]

    
        
        