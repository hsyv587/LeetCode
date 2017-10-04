class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        12345
        x1234
        -----
        
        '''
        if not num1 or not num2:
            return '0'
        res = ''
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        pres = 0
        total_carry = 0
        while True:
            pres += 1
            if pres <= len(num1):
                p1 = len(num1) - pres
                p2 = len(num2) - 1
                current_sum = total_carry
                for i in range(min(pres, len(num2))):
                    current_sum += int(num1[p1]) * int(num2[p2])
                    p1 += 1
                    p2 -= 1
                res += str(current_sum % 10)
                total_carry = current_sum / 10
            else:
                p1, p2 = 0, len(num1) + len(num2) - pres - 1
                current_sum = total_carry
                for i in range(len(num1) + len(num2) - pres):
                    current_sum += int(num1[p1]) * int(num2[p2])
                    p1 += 1
                    p2 -= 1
                res += str(current_sum % 10)
                total_carry = current_sum / 10
            if pres == len(num1) + len(num2) - 1:
                if total_carry:
                    res += str(total_carry)
                start = 0
                res = res[::-1]
                for i in res:
                    if i == '0':
                        start += 1
                    else:break
                #print res
                return res[min(start, len(res) - 1):]
                    
        
            
            
                
        