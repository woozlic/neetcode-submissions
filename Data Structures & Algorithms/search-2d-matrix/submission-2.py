class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            res = self.binarySearch(matrix[m], target)
            if res != -1:
                return True
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        return False


    @staticmethod
    def binarySearch(lst: List[int], target):
        l, r = 0, len(lst) - 1
        while l <= r:
            m = (l+r) // 2
            if lst[m] < target:
                l = m + 1
            elif lst[m] > target:
                r = m - 1
            else:
                return m
        return -1