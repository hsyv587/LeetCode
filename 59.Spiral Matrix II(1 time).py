class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(n)] for i in range(n)]
        i, j = 0, 0
        direct = 'right'
        for c in range(1, n * n + 1):
            res[i][j] = c
            if direct == 'right':
                if j < n - 1 and res[i][j + 1] == 0:
                    j += 1
                else:
                    i += 1
                    direct = 'down'
            elif direct == 'down':
                if i < n - 1 and res[i + 1][j] == 0:
                    i += 1
                else:
                    j -= 1
                    direct = 'left'
            elif direct == 'left':
                if j > 0 and res[i][j - 1] == 0:
                    j -= 1
                else:
                    i -= 1
                    direct = 'up'
            elif direct == 'up':
                if i > 0 and res[i - 1][j] == 0:
                    i -= 1
                else:
                    j += 1
                    direct = 'right'
        return res
                