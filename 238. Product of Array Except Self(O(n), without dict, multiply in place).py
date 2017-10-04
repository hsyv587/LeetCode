class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''Basically the same thought as using dict, but instead it stores the left side production directly on the output list, and multiply the right side prodcution in reverse order and in-place, '''
        length = len(nums)
        result = []
        prod = 1
        for i in range(length):
            result.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(length - 1, -1, -1):
            result[i] *= prod
            prod *= nums[i]
        return result
         