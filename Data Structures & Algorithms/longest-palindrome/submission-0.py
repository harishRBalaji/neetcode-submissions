class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        result = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                result += 2
        
        for cnt in count.values():
            if cnt % 2 == 1:
                result += 1
                break
        
        return result