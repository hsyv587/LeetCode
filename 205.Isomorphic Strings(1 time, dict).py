class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        res1 = []
        res2 = []
        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]].append(i)
            else:
                dic1[s[i]] = [i]
            if t[i] in dic2:
                dic2[t[i]].append(i)
            else:
                dic2[t[i]] = [i]
        for i in dic1:
            res1.append(dic1[i])
        for i in dic2:
            res2.append(dic2[i])
        res1.sort()
        res2.sort()
        #print res1, res2
        return res1 == res2