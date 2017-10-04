class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            t_res = self.threeSum(nums, target - nums[i], i)
            if t_res:
                for i in t_res:
                    res.append(i)
        return res
                
        
    def threeSum(self, nums, target, index):
        t_res = []
        for i in range(index + 1, len(nums) - 2):
            if i != index + 1 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                t_sum = nums[i] + nums[left] + nums[right]
                if t_sum == target:
                    t_res.append([nums[index], nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif t_sum < target:
                    left += 1
                elif t_sum > target:
                    right -= 1
        return t_res
            