class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                        continue
                    else:
                        return False
                else:
                    j -= 1
            else:
                i += 1
        return True