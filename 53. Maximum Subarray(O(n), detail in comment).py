class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        if a[i:j] is the max one, then any part ending with a[i - 1]will be negative,
        so max_curr will be negative when reach index i - 1, 
        since a[i] must be positive, max_curr must restart at a[i].
        And since any part start with a[i] is smaller than a[i:j], 
        the max_so_far will record a[i:j]
        '''
        if not nums:
            return None
        max_so_far = nums[0]
        max_curr = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], nums[i] + max_curr)
            max_so_far = max(max_curr, max_so_far)
        return max_so_far
            
            
        
        