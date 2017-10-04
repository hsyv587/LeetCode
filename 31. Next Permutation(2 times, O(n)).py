class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        if pivot != -1:
            #print pivot
            switched = len(nums) - 1
            for i in range(len(nums) - 1, pivot, -1):
                #print nums[i], nums[pivot]
                if nums[i] > nums[pivot]:
                    switched = i
                    break
            nums[switched], nums[pivot] = nums[pivot], nums[switched]
            #print switched
        i, j = pivot + 1, len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
                
        
        