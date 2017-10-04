class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        leftRow, rightRow = 0, len(matrix) - 1
        while leftRow <= rightRow:
            midRow = leftRow + (rightRow - leftRow) / 2
            if leftRow == rightRow:
                return self.searchCol(matrix[midRow], target)
            if not matrix[midRow]:
                del matrix[midRow]
                rightRow -= 1
                continue
            if matrix[midRow][0] > target:
                rightRow = midRow
            elif matrix[midRow][-1] < target:
                leftRow = midRow + 1
            else:
                if target == matrix[midRow][0] or target == matrix[midRow][-1]:
                    return True
                else:
                    return self.searchCol(matrix[midRow], target)
        return False
    def searchCol(self, line, target):
        left, right = 0, len(line) - 1
        while left <= right:
            if left == right:
                if line[left] != target:
                    return False
            mid = left + (right - left) / 2
            if line[mid] == target:
                return True
            elif line[mid] < target:
                left = mid + 1
            else:
                right = mid
        return False