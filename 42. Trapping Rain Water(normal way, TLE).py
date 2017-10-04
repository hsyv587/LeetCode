class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        last_line, line = 0, 1
        result = 0
        while True:
            left = -1
            current_lowest = -1
            for i in range(len(height)):
                if height[i] >= line:
                    if height[i] > line:
                        if current_lowest == -1:
                            current_lowest = i
                        elif height[i] < height[current_lowest]:
                            current_lowest = i
                    
                    if left == -1:
                        left = i
                    else:
                        result += (i - left - 1) * (line - last_line)
                        left = i
                        #print result
            if current_lowest == -1:
                break
            last_line = line
            line = height[current_lowest]
        return result
                    
        