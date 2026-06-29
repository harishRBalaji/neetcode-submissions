class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        result = []
        for key, value in dict.items():
            if value > (len(nums) // 3):
                result.append(key)
        
        return result
        