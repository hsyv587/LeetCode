class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' or not s[i].isalpha():
                if length != 0:
                    return length
                else:
                    continue
            if s[i].isalpha():
                length += 1
        return length