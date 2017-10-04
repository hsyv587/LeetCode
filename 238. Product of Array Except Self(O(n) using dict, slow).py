class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mul_dic = {(0, -1) : 1,
                   (len(nums), len(nums) - 1) : 1}
        result = []
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            left_prod *= nums[i]
            right_prod *= nums[len(nums) - i - 1]
            mul_dic[(0, i)] = left_prod
            mul_dic[(len(nums) - i - 1, len(nums) - 1)] = right_prod
        #print mul_dic
        for i in range(len(nums)):
            result.append(0)
            result[i] = mul_dic[(0, i - 1)] * mul_dic[(i + 1, len(nums) - 1)]
        return result
         