class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_house(money):
            n = len(money)
            if not money:
                return 0
            if len(money) == 1:
                return money[0]
            
            dp = [0] * n
            dp[0] = money[0]
            dp[1] = max(money[0], money[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
            return dp[n - 1]
        
        return max(rob_house(nums[1:]), rob_house(nums[:-1]))