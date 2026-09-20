class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_vs_index_map = {}

        for i in range(len(nums2)):
            num_vs_index_map[nums2[i]] = i
        
        result = []

        for i in range(len(nums1)):
            index = num_vs_index_map[nums1[i]]
            j = index + 1
            while j < len(nums2):
                if nums2[j] > nums2[index]:
                    result.append(nums2[j])
                    break
                j += 1
            if j == len(nums2):
                result.append(-1)
        
        return result
            