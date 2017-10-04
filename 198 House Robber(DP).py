class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        return 0 if not nums else self.rec_call(nums, 0, table)
    
    def rec_call(self, nums, current, table):
        length = len(nums)
        if length in table:
            return current + table[length]
        
        max1, max2 = 0, 0
        if length <= 2:
            max1 = current + nums[0]
        else:max1 = self.rec_call(nums[2:], current + nums[0], table)
            
        if length >= 2:
            if length <= 3:
                max2 = current + nums[1]
            else:max2 = self.rec_call(nums[3:], current + nums[1], table)
        #print current, nums, max1, max2, table
        temp_max = max(max1, max2)
        table[length] = temp_max - current
        return temp_max