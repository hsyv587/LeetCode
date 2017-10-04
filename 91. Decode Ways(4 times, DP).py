class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        table = {}
        return self.rec(s, table)
    
    def rec(self, s, table): 
        #print s, table
        if s and s[0] == '0':
            return 0
        if len(s) == 1 or len(s) == 0:
            return 1
        if len(s) in table:
            return table[len(s)]
        result = 0
        if int(s[0]) * 10 + int(s[1]) <= 26:
            result += self.rec(s[2:], table)
        if s[1] != '0':
            result += self.rec(s[1:], table)
        table[len(s)] = result
        return result