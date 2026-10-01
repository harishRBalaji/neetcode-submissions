class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_map = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        
        for val in count_map.values():
            if val % 2 == 1:
                return False
        
        return True