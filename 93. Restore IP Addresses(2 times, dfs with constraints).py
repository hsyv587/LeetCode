class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.rec(s[:], res, 4, [])
        return res
    def rec(self, s, res, remain_digits, t_res):
        if remain_digits == 1:
            if int(s) > 255 or (len(s) > 1 and s[0] == '0'):
                return 0
            t = ''
            for i in t_res:
                t += i + '.'
            res.append(t + s)
        
        for i in range(max(0, len(s) - 3*(remain_digits - 1) - 1), min(3, len(s) - remain_digits + 1)):
            if i == 2 and int(s[:i + 1]) > 255:
                break
            if i and s[0] == '0':
                break
            t_t_res = t_res[:]
            t_t_res.append(s[:i + 1])
            self.rec(s[i + 1:], res, remain_digits - 1, t_t_res)