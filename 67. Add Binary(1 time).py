class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        pa, pb = len(a) - 1, len(b) - 1
        carry = 0
        res = ''
        while pa >= 0 and pb >= 0:
            t_sum = int(a[pa]) + int(b[pb]) + carry
            t_res = t_sum % 2
            carry = 1 if t_sum >= 2 else 0
            res += str(t_res)
            pa -= 1
            pb -= 1
        while pa >= 0:
            t_sum = int(a[pa]) + carry
            t_res = t_sum % 2
            carry = 1 if t_sum >= 2 else 0
            res += str(t_res)
            pa -= 1
        while pb >= 0:
            t_sum = int(b[pb]) + carry
            t_res = t_sum % 2
            carry = 1 if t_sum >= 2 else 0
            res += str(t_res)
            pb -= 1
        if carry == 1:
            res += '1'
        return res[::-1]
            
            