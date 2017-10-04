class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        left, right = 0, 0
        self.rec_call(n, left, right, '', result)
        return result
        
    def rec_call(self, n, left, right, s, result):
        if left < n:
            self.rec_call(n, left + 1, right, s + '(', result)
        if right < n and left > right:
            self.rec_call(n, left, right + 1, s + ')', result)
        if left == right == n:
            result.append(s)