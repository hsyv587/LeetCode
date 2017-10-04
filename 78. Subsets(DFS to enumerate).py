class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = nums[:]
        result = []
        self.rec_call([], temp, result)
        return result
    
    def rec_call(self, current, remains, result):
        if len(remains) == 0:
            result.append(current)
        else:
            self.rec_call(current, remains[1:], result)
            current2 = current[:]
            current2.append(remains[0])
            self.rec_call(current2, remains[1:], result)