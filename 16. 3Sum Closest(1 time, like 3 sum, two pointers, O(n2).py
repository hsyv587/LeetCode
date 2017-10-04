class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = pow(2, 32) - 1
        res = 0
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                t_sum = nums[i] + nums[left] + nums[right]
                t_diff = t_sum - target
                if abs(t_diff) < min_diff:
                    min_diff = abs(t_diff)
                    res = t_sum
                if t_diff < 0:
                    left += 1
                elif t_diff > 0:
                    right -= 1
                else:
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
        