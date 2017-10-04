class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #if repeated, only add this number to the previous added res, otherwise add to all of previous res
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                lens = len(res)
                for j in range(last_added, len(res)):
                    res.append(res[j] + [nums[i]])
                last_added = lens
            else:
                last_added = len(res)
                for j in range(len(res)):
                    res.append(res[j] + [nums[i]])                
        return res
        