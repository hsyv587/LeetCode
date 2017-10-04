class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = self.rec_call(nums, 0, len(nums) - 1)
        return sum(nums[left : right + 1])
    
    
    def rec_call(self, nums, left, right):
        if right == left:
            return left, right
        left_left, left_right = self.rec_call(nums, left, (left + right) / 2)
        right_left, right_right = self.rec_call(nums, (left + right) / 2 + 1, right)
        temp_left, temp_right = (left + right) / 2, (left + right) / 2 + 1
        temp_sum = 0
        temp_max = -pow(2,32) + 1
        while temp_left >= left:
            temp_sum += nums[temp_left]
            if temp_sum > temp_max:
                temp_max = temp_sum
                mid_left = temp_left
            temp_left -= 1
            
        temp_sum = 0
        temp_max = -pow(2,32) + 1
        while temp_right <= right:
            temp_sum += nums[temp_right]
            if temp_sum > temp_max:
                temp_max = temp_sum
                mid_right = temp_right
            temp_right += 1
        left_sum = sum(nums[left_left : left_right + 1])
        right_sum = sum(nums[right_left : right_right + 1])
        mid_sum = sum(nums[mid_left : mid_right + 1])
        if left_sum >= max(right_sum, mid_sum):
            return left_left, left_right
        elif mid_sum >= max(left_sum, right_sum):
            return mid_left, mid_right
        else:
            return right_left, right_right
            
        
        