class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return (1 / x if n == -1 else 1) if n == 0 or n == -1 else (self.myPow(x * x, n / 2) * ([1 , x][n % 2]))