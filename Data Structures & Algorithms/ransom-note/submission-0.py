class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for c in count_ransom:
            if count_magazine[c] < count_ransom[c]:
                return False
        
        return True