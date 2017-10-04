class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_s = ''
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                temp_s += ch
        clean_s = temp_s.lower()
        #print clean_s
        
        if len(clean_s) == 0:
            return True
        
        for i in range(len(clean_s) / 2):
            if clean_s[i] != clean_s[len(clean_s) - i - 1]:
                return False
        return True
                
            