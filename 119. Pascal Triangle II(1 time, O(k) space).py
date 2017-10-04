class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row0 = [1]
        row1 = []
        for i in range(rowIndex):
            row1 = [1 for k in range(i + 2)]
            for j in range(1, i + 1):
                row1[j] = row0[j - 1] + row0[j]
            row0 = row1
        return row0
                
        