class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        si = 1
        sd = 1
        result = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                si, sd = si + 1, 1
            elif nums[i] < nums[i - 1]:
                si, sd = 1, sd + 1
            else:
                si, sd = 1, 1
            
            result = max(result, si, sd)
        
        return result
                    