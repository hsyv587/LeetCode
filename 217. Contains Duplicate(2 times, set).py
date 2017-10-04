class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = set()
        for i in nums:
            if i in dic:
                return True
            else:
                dic.add(i)
        return False