class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            width = j-i
            height = min(heights[i], heights[j])
            area = self.get_area(width, height)
            max_area = max(area, max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
    
    @staticmethod
    def get_area(width: int, height: int) -> int:
        return width * height
