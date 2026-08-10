class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_maximum, suffix_maximum = [0] * n, [0] * n

        prefix_maximum[0] = height[0]
        for i in range(1, n):
            prefix_maximum[i] = max(prefix_maximum[i - 1], height[i])
        
        suffix_maximum[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_maximum[i] = max(suffix_maximum[i + 1], height[i])
        
        result = 0
        for i in range(n):
            result += min(prefix_maximum[i], suffix_maximum[i]) - height[i]
        
        return result
        



        