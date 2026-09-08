class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1 # maximum element found while traversing the array from the right
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = max_right
            max_right = max(curr, max_right)
        
        return arr