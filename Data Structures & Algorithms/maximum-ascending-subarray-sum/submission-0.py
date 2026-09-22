class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                current_sum = 0
            
            current_sum += nums[i]
            result = max(result, current_sum)
        
        return result