class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        table = {}
        return self.rec(s, wordDict, table)
        
    def rec(self, s, wordDict, table):
        if len(s) in table:
            return table[len(s)]
        for i in wordDict:
            #print s, s[0 : len(i)], i
            if s[0 : len(i)] == i:
                if len(s) == len(i):
                    return True
                else:
                    if self.rec(s[len(i):], wordDict, table):
                        return True
        table[len(s)] = False
        #print table
        return False

        
        