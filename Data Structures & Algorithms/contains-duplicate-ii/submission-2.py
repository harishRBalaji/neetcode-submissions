class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary and abs(i - dictionary[nums[i]]) <= k:
                return True
            dictionary[nums[i]] = i
        return False

