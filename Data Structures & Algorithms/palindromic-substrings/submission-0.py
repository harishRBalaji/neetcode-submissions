class Solution:
    def countSubstrings(self, s: str) -> int:
        result_index, result_length = 0, 0
        count = 0
        def helper(left, right):
            nonlocal s, result_index, result_length, count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            left, right = i, i
            helper(left, right)
            left, right = i, i + 1
            helper(left, right)
        
        return count
        