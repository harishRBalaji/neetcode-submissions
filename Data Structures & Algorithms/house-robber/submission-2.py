class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        
        rob_1, rob_2 = 0, 0

        for num in nums:
            temp = max(num + rob_1, rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return rob_2