class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        table = {}
        res = []
        self.rec(s[:], res, [], table)
        #print table
        return res
    def rec(self, s, res, t_res, table):
        if not s:
            res.append(t_res)
            return 0
        for i in range(len(s)):
            if self.is_palin(s[:i + 1], table):
                self.rec(s[i + 1:], res, t_res[:] + [s[:i + 1]], table)
        
    def is_palin(self, s, table):
        if s in table:
            return table[s]
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                table[s] = False
                return False
            i += 1
            j -= 1
        table[s] = True
        return True