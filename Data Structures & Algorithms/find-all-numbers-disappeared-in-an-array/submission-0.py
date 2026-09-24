class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        index = 0
        n = len(nums)
        result = []
        for num in range(1, n + 1):
            while index < n and nums[index] < num:
                index += 1
            if index == n or nums[index] > num:
                result.append(num)
        
        return result
                