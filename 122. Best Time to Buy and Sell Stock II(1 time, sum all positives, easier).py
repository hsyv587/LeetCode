class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
        result = 0
        for i in diff:
            if i > 0:
                result += i
        return result