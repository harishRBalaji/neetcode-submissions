class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decode_current, decode_next, decode_next_next = 1, 1, 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                decode_current = 0
            else:
                decode_current = decode_next
            
            if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                decode_current += decode_next_next
            decode_next_next = decode_next
            decode_next = decode_current
        return decode_current