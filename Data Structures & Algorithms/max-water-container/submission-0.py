class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l < r:
            width = min(heights[l], heights[r])
            length = r - l
            if width * length > max_volume:
                max_volume = width * length
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_volume

        