class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        table = {}
        self.rec_call([], candidates, target, result, table)
        return result
        
    def rec_call(self, current, candidates, remain, result, table):
        for i in range(len(candidates)):
            temp = remain - candidates[i]
            temp_current = current[:]
            temp_current.append(candidates[i])
            if temp == 0:
                result.append(temp_current)
                continue
            if temp < 0:
                break
            #print result
            self.rec_call(temp_current, candidates[i:], remain - candidates[i], result, table)
        