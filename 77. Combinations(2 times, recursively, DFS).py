class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i + 1 for i in range(n)]
        res = []
        self.rec(nums[:], k, res, [])
        return res
    
    def rec(self, nums, remainK, res, t_res):
        if remainK == 0:
            res.append(t_res)
            return 0
        for i in range(len(nums) - remainK + 1):
            t_t_res = t_res[:]
            t_t_res.append(nums[i])
            self.rec(nums[i + 1:], remainK - 1, res, t_t_res)
        