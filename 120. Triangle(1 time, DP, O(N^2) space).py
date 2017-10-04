class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        if not triangle:
            return 0
        table = {}
        return self.rec(triangle, 0, 0, table)

    def rec(self, triangle, row, index, table):
        #print row+ 1 , index + 1
        if (row, index) in table:
            return table[(row, index)]
        if row == len(triangle) - 1:
            return triangle[row][index]
        min_sum = triangle[row][index] + min(self.rec(triangle, row + 1, index, table), self.rec(triangle, row + 1, index + 1, table))
        table[(row, index)] = min_sum
        return min_sum
        