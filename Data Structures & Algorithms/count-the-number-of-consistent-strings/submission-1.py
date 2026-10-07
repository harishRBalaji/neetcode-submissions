class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        allowed_characters_set = set(allowed)

        for word in words:
            flag = 1
            for c in word:
                if c not in allowed:
                    flag = 0
                    break
            count += flag
        
        return count