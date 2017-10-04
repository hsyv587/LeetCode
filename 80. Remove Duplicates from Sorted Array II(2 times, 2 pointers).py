class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        p1, p2 = 1, 2
        curr_count = 0
        for i in range(len(nums) - 2):
            if nums[p2] == nums[p1] and nums[p1] == nums[p1 - 1]:
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
        return p1 + 1