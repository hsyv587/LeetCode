class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search
        if len(nums) <= 1:
            return -1
        left, right = 1, len(nums) - 1
        mid = (right + left) / 2
        count = 0
        for i in range(100):
            #print left, right
            if right == left:
                return right
            for i in nums:
                if i <= mid and i >= left:
                    count += 1
            if count > (right - left + 2) / 2:
                right = mid
            else:left = mid + 1
            mid = (right + left) / 2
            #print count
            count = 0