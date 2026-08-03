class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_length, result_index = 0, 0
        for i in range(len(s)):
            def helper(left, right):
                nonlocal s, result_length, result_index
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if (right - left + 1) > result_length:
                        result_length = right - left + 1
                        result_index = left
                    left -= 1
                    right += 1
            
            left, right = i, i
            helper(left, right)
            left, right = i, i + 1
            helper(left, right)
        
        return s[result_index : result_index + result_length]