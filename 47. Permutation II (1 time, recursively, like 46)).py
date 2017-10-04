class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        self.rec(nums[:], [], res)
        return res
    
    def rec(self, remain, t_res, res):
        if len(remain) == 1:
            t_t_res = t_res[:]
            t_t_res.append(remain[0])
            res.append(t_t_res)
            return 0
        for i in range(len(remain)):
            if i and remain[i] == remain[i - 1]:
                continue
            t_t_res = t_res[:]
            t_t_res.append(remain[i])
            if i == 0:
                self.rec(remain[1: ], t_t_res, res)
            elif i == len(remain) - 1:
                self.rec(remain[: i], t_t_res, res)
            else:
                self.rec(remain[: i] + remain[i + 1 :], t_t_res, res)
            