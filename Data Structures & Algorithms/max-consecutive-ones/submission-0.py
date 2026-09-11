class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = count = 0

        for num in nums:
            count = count + 1 if num else 0
            max_ones = max(max_ones, count)
        
        return max_ones