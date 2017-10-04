class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = {}
        return self.rec_call(n, table)
    
    
    def rec_call(self, remain, table):
        if remain in table:
            return table[remain]
        result = 0
        if remain >= 2:            
            result += self.rec_call(remain - 2, table)
        if remain >= 1:
            result += self.rec_call(remain - 1, table)
        if remain == 0:
            return 1
        table[remain] = result
        return result
        
        