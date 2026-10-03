class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency_map = Counter(arr)

        lucky_integer = -1

        for key, val in frequency_map.items():
            if key == val:
                lucky_integer = max(lucky_integer, key)
        
        return lucky_integer