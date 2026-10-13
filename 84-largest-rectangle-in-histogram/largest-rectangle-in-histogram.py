class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        n = len(heights)
        area = 0
        for i in range(n+1):
            curr_height = heights[i] if i<n else 0
            while stack and heights[stack[-1]] > curr_height:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = max(area,h * width)
            if i < n:
                stack.append(i)
        return area
