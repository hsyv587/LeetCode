class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        p1, p2 = 0, len(s) - 1
        while True:
            #print s[p1], s[p2]
            if p1 > p2:
                break
            while ((not s[p1].isdigit()) and (not s[p1].isalpha())) or (s[p1] == ' '):
                p1 += 1
                if p1 >= len(s):
                    return True
                #print p1
            while ((not s[p2].isdigit()) and (not s[p2].isalpha())) or (s[p2] == ' '):
                p2 -= 1
                if p2 < 0:
                    return True
                #print p2
            if p1 == p2:
                return True
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
            
                
            