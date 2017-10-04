class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_dic = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        total_len = 1
        result = []
        if len(digits) == 0:
            return []
        for i in digits:
            total_len *= len(map_dic[i])
        for i in range(total_len):
            temp_len = total_len
            result.append('')
            for j in range(len(digits)):
                temp_len /= len(map_dic[digits[j]])
                result[i] += map_dic[digits[j]][(i / temp_len) % len(map_dic[digits[j]])]
        return result