#-*- coding:utf-8 -*-
import sys
import os
import time

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = nums[i] * -1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[left], nums[right], -target])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif nums[left] + nums[right] <= target:
                    left += 1
                else:
                    right -= 1
        return result

if __name__ == "__main__":
    start =time.time()
    nums = [0,0,0]
    solution = Solution()
    result = solution.threeSum(nums)
    stop = time.time()
    print stop - start, result
