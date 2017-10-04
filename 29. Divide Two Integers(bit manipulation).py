class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        remain = dividend
        result = 0
        while remain >= divisor:
            temp, i = divisor, 0
            while remain >= temp:
                if (remain - temp) < temp:
                    break
                temp <<= 1
                i += 1
            remain -= temp
            result += (1 << i)
        result *= (1 if flag else -1)
        return min(max(-2147483648, result), 2147483647)