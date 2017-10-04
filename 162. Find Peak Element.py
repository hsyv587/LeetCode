class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        while True:
            mid = left + (right - left) / 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            else:
                return mid
