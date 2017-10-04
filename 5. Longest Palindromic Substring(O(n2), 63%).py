#-*- coding:utf-8 -*-
import sys
import os

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_sub = ''
        max_len = 0
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            left, right = i, i
            while left - 1 >= 0 and right + 1 <= len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if 1 + right - left > max_len:
                max_len = 1 + right - left
                max_sub = s[left:right + 1]

            left, right = i, i + 1
            if s[left] == s[right]:
                while left - 1 >= 0 and right + 1 <= len(s) - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                if 1 + right - left > max_len:
                    max_len = 1 + right - left
                    max_sub = s[left:right + 1]
        return max_sub

if __name__ == "__main__":
    import time
    start =time.time()
    s = 'dabaabd'
    solution = Solution()
    result = solution.longestPalindrome(s)
    stop = time.time()
    print stop - start, result