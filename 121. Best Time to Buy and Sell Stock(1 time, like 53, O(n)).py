class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
        
        max_curr, max_so_far = 0, 0
        #print diff
        for i in range(1, len(diff)):
            max_curr = max(0, max_curr + diff[i])
            max_so_far = max(max_curr, max_so_far)
        return max_so_far