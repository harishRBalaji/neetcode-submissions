class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum, current_sum = nums[0], 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum