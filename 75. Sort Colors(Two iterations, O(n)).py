class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, 0
        for x in range(len(nums)):
            if nums[x] == 0:
                i += 1
                j += 1
                k += 1
            elif nums[x] == 1:
                j += 1
                k += 1
            elif nums[x] == 2:
                k += 1
        
        for x in range(len(nums)):
            if x < i:
                nums[x] = 0
            elif x < j:
                nums[x] = 1
            elif x < k:
                nums[x] = 2
                