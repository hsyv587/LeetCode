class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.rec(candidates[:], result, 0, target, [])
        return result
        
    def rec(self, candidates, result, curr_sum, target, curr_res):
        for i in range(len(candidates)):
            if i and candidates[i] == candidates[i - 1]:
                continue
            if curr_sum + candidates[i] > target:
                break
            t_res = curr_res[:]
            t_res.append(candidates[i])
            if curr_sum + candidates[i] == target:
                result.append(t_res)
            self.rec(candidates[i + 1 : ], result, curr_sum + candidates[i], target, t_res)
            