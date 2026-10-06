class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_vs_index_list_map = {}

        for i in range(len(nums)):
            if nums[i] not in num_vs_index_list_map:
                num_vs_index_list_map[nums[i]] = []
                num_vs_index_list_map[nums[i]].append(i)
            else:
                num_vs_index_list_map[nums[i]].append(i)
        
        pairs = 0

        for v in num_vs_index_list_map.values():
            pairs += math.comb(len(v), 2)
        
        return pairs